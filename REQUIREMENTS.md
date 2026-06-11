# Political Strategy Game - Prototype Requirements

## 1. Development Strategy

### Phase 1: Spring Java Backend + MongoDB + Python Test UI

Build the complete gameplay simulation as a Spring Java backend first, with MongoDB used for persistent game state and editable game content/rules. A lightweight Python UI is used for testing and rapid gameplay iteration.

Purpose:

- Rapidly test mechanics.
- Balance party stats, cards, news reactions, and elections.
- Develop AI behavior.
- Refine narrative and public memory systems.
- Validate the endless gameplay loop.

The prototype UI should not be CLI-first. It should be a simple card-game-style Python UI for testing the backend, with visible party health, cards, news reactions, and special actions.

MongoDB should store:

- Active game state for each player/game.
- Party state, public state, current turn, pending effects, and history.
- Card definitions.
- News definitions.
- Special action definitions.
- Scenario definitions.
- Ideology definitions.
- Balancing/rule configuration.

YAML or JSON files may still be used as seed/import files during development, but the backend should load active rules and content from MongoDB so gameplay can be changed without rebuilding the backend.

### Phase 2: Mobile Port

Once gameplay is stable, port the player-facing UI to Flutter/Dart.

Target platform:

- Offline mobile game.
- Android first.
- iOS possible later.

Architecture should stay modular so the Spring backend rules, metadata, and balancing decisions can be reused or recreated cleanly for mobile.

## 2. Core Concept

The game is an endless, turn-based political strategy simulation inspired by Indian state elections.

The player controls one fictional political party and competes against an AI-controlled rival party. Parties use fictional animal-themed names, not real party names.

Example party names:

- Tiger Front
- Elephant Congress
- Peacock Party
- Bull Alliance
- Cobra Sena
- Deer Democratic Party

The player may start as either:

- Government party
- Opposition party

The public acts as a hidden third player. Public support is visible, but deeper public memory and mood drivers are partly hidden.

## 3. Time And Election Cycle

Each election cycle lasts 60 turns.

- 1 turn = 1 month.
- Example: if the game starts in October 2020, the next turn is November 2020.
- A mandatory election occurs after 60 turns unless the government falls earlier.
- If the government falls, an early election is called.
- After each election, the winning party forms government and the losing party becomes opposition.
- The game continues endlessly across election cycles.

There is no final victory condition. The goal is to survive, form government, retain power, or return to power over repeated political cycles.

## 4. Game Over

The player loses if their party collapses.

Game over conditions:

- Player party coins reach 0 or below.
- Player party public support falls below 10%.
- Player party morale falls below 10%.

## 5. MVP Actors

MVP contains:

- Public
- Government party
- Opposition party
- Third party

The game supports exactly three political parties in the MVP. Each party may be controlled by a human or computer, but only these controller mixes are allowed:

- 1 human + 2 computer
- 2 human + 1 computer

Regional parties, independents, and coalition partners beyond the third party may still be abstracted through coalition readiness and smaller-party support.

## 6. Party Stats

Each party has the following visible stats.

### Core Party Stats

| Stat | Type | Purpose |
|---|---|---|
| Coins | Currency | Spendable fictional money used for cards and actions |
| Party Morale | 0-100 | Worker energy, internal confidence, and discipline |
| Corruption Score | 0-100 | Higher means more corruption risk/suspicion |
| Media Image | 0-100 | How favorable or competent the party appears in media |
| Public Support | 0-100 | Vote-share-like public support |

All cards, news reactions, and special actions should be able to affect these stats.

### Public Support

Public support is shown as vote share.

Example:

| Group | Support |
|---|---:|
| Government | 42% |
| Opposition | 34% |
| Undecided | 24% |

Public support should not overreact to a single action. Repeated behavior, scandals, ideology mismatch, and crisis handling should matter over time.

## 7. Hidden Public Memory

The public has hidden memory variables that influence future reactions.

Possible hidden memory fields:

- Trust memory for government
- Trust memory for opposition
- Anti-incumbency
- Scandal fatigue
- Corruption suspicion against government
- Corruption suspicion against opposition
- Protest fatigue
- Governance satisfaction
- Civic service memory
- Ideology consistency memory
- Money power suspicion
- Issue salience for jobs, price rise, corruption, education, health, regional pride, identity, and welfare

The player may receive hints through opinion polls, headlines, or public mood summaries, but should not always see exact hidden values.

## 8. Ideology System

At party creation, the player chooses a base ideology.

MVP ideology options:

- Welfare Populist
- Development First
- Regional Pride
- Anti-Corruption
- Identity Politics
- Unity Platform

Ideology affects:

- Card effectiveness.
- Public interpretation.
- Party morale.
- Trust over time.

If the player repeatedly takes actions that contradict the chosen ideology:

- Party morale drops.
- Internal support may drop.
- Trust may suffer.
- Public may see the party as opportunistic.

Cards and news reactions should include ideology tags so the engine can check alignment.

## 9. Government Vs Opposition Asymmetry

Government and opposition have different strengths, risks, and card pools.

### Government Advantages

- More coins.
- Governance powers.
- More media access.
- Administrative control.
- Higher initial trust in some scenarios.

### Government Risks

- Anti-incumbency.
- Corruption exposure.
- Public fatigue.
- Accountability for crises.

### Opposition Advantages

- Easier protests and movements.
- Anti-corruption narrative.
- Movement building.
- Reform momentum.

### Opposition Weaknesses

- Fewer coins.
- Lower initial trust.
- Less media reach.
- Higher risk if accusations fail.

Government may also use agitation-like actions, but these should usually target the opponent's scores rather than create anti-incumbency.

## 10. Turn Flow

Each turn represents one month and contains several screens/phases.

### Screen 1: Card Table / Status Dashboard

Show:

- Current month and year.
- Current turn in election cycle.
- Election deadline.
- Player role.
- Government and opposition party names.
- Public support.
- Player health/stats panel.
- Opponent health/stats panel.
- Stat movement from previous turns.
- Pending delayed card/news/action results.
- Last discovered results.
- No-confidence availability.
- Current hand/deck view for the player's role.

The UI should feel more like a card game than a text console. Party health should be shown as prominent stat bars or panels for coins, party morale, corruption score, media image, and public support.

### Screen 2: News Reaction

Each turn has two news items:

1. External/historical-inspired monthly news.
2. Internal/game-generated news based on what happened last turn.

The player chooses one reaction for each news item.

Each news item has 4 reaction choices. Each reaction affects:

- Player party morale.
- Player corruption score.
- Player media image.
- Player public support.

News reactions may also create hidden public memory effects.

### Screen 3: Main Political Card

The player chooses one main political card from their role deck.

The player can see all available cards for their side. Cards are not hidden draws in the MVP.

### Screen 4: Strategic / Special Action

The player chooses one special action, such as polling, media campaign, investigation, coalition talk, or no-confidence motion.

Special actions are not cards. They are system actions that may be always available or conditionally unlocked.

No-confidence is treated as a normal special action in this list. It should not require a separate button or separate UI flow.

### Screen 5: Results / Month End

Show:

- Newly discovered effects from previous turns.
- AI actions.
- Updated stats and trends.
- Newly pending outcomes.
- Month advancement.

## 11. Card-Game UI Screen Concept

```text
====================================================================
 POLITICAL STRATEGY SIM                         Turn 14 / Month 14
 State: Dakshin Pradesh                         Date: Nov 2021
 Player: Elephant Congress                      Role: Opposition
====================================================================

TOP BAR
--------------------------------------------------------------------
Government: Tiger Front        Opposition: Elephant Congress
Election Due: Oct 2025         Special Action: No-Confidence Locked
Reason: Govt popularity above 30% / Govt morale stable

PARTY HEALTH PANELS
--------------------------------------------------------------------
PLAYER - Elephant Congress
Coins             [###########.........] 118   -12
Party Morale      [############........]  64    +2
Corruption Score  [###.................]  18     0
Media Image       [###########.........]  57    +4
Public Support    [#######.............]  34%   +3

GOVT - Tiger Front
Coins             [################....] 210    -8
Party Morale      [##############......]  71    -3
Corruption Score  [########............]  42    +5
Media Image       [#########...........]  48    -4
Public Support    [########............]  42%   -2

PUBLIC MOOD PANEL
--------------------------------------------------------------------
Undecided Support: 24%   (-1)
Public Mood: Restless
Main Issues: Jobs, Price Rise, Corruption Rumours
Memory Hint: Voters are noticing repeated corruption attacks.

RECENT STAT MOVEMENT
--------------------------------------------------------------------
Player Morale      59 -> 62 -> 64
Player Media       49 -> 53 -> 57
Govt Corruption    33 -> 37 -> 42
Govt Media         56 -> 52 -> 48

PENDING RESULTS
--------------------------------------------------------------------
1. Expose Teacher Admission Scam
   Expected Result Window: Dec 2021 - Mar 2022
   Status: Public discussion growing

2. Student Movement
   Expected Result Window: Nov 2021 - Jan 2022
   Status: Campus response unclear

PLAYER CARD ROW
--------------------------------------------------------------------
[01] Anti-Corruption March     Cost 10   Risk Medium
     Agitation / Movement      Target: Govt + Public
     Result Window: 1-3 months

[02] Cleanliness Drive         Cost 8    Risk Low
     Positive / Service        Target: Public + Self
     Result Window: 1-3 months

[03] Expose Admission Scam     Cost 14   Risk High
     Scandal / Accusation      Target: Govt
     Result Window: 2-5 months

NEWS REACTION CARDS
--------------------------------------------------------------------
External News: Fuel prices rise across the state.
[A] Blame Govt   [B] Promise Relief   [C] Demand Inquiry   [D] Stay Silent

Internal News: Student movement response remains unclear.
[A] Support Students   [B] Ask For Calm   [C] Attack Govt   [D] Avoid Comment

SPECIAL ACTION ROW
--------------------------------------------------------------------
[1] Conduct Poll   [2] Media Campaign   [3] Investigate Scandal
[4] Coalition Talk [5] No-Confidence    [6] Fundraising Drive
====================================================================
```

Screen requirement:

- Main gameplay should look and feel like a card table.
- Player and opponent health must be visible at all times.
- Cards should show category, cost, target, risk, and result window.
- News reactions should be presented like choice cards.
- Special actions should appear as a normal action row, including no-confidence when unlocked.

## 12. Card System

Each party starts each cycle with a role-specific deck of 30 cards.

The government deck and opposition deck are separate.

Cards can have:

- Costs.
- Visible delayed effects.
- Hidden delayed effects.
- Risk rolls.
- Chance-based outcomes.
- Ideology tags.
- Role restrictions.
- Targeting rules.

Card results are not discovered immediately. The earliest discovery is the next turn.

Effect timing rules:

- Minimum delay: 1 turn.
- Maximum delay: 5 turns.
- Some cards resolve in 1 month.
- Some cards resolve randomly over 2-5 months.
- Scandals, movements, and governance projects often have delayed outcomes.

## 13. Card Categories

MVP card categories:

| Category | Purpose |
|---|---|
| Positive / Service | Build goodwill through constructive public work |
| Governance | Use state power to deliver policy or administration |
| Agitation / Movement | Mobilize people around issues or against another party |
| Scandal / Accusation | Attack opponent credibility through wrongdoing claims |
| Defensive / Counter | Respond to attacks, scandals, or negative narratives |
| Media / Narrative | Shape public perception and news cycle |
| Organization / Resource | Strengthen party machinery or raise coins |
| Ideology / Identity | Appeal to ideological or social blocs |
| Constitutional / Power Move | No-confidence or government-changing mechanics |

Future categories:

- Coalition / Defection
- Crisis Response
- Election Campaign

## 14. Deck Balance

### Government Deck Distribution

| Category | Count |
|---|---:|
| Governance | 8 |
| Positive / Service | 4 |
| Defensive / Counter | 5 |
| Media / Narrative | 3 |
| Organization / Resource | 4 |
| Ideology / Identity | 2 |
| Agitation / Movement | 1 |
| Scandal / Accusation | 3 |
| Total | 30 |

### Opposition Deck Distribution

| Category | Count |
|---|---:|
| Scandal / Accusation | 7 |
| Defensive / Counter | 5 |
| Agitation / Movement | 5 |
| Positive / Service | 5 |
| Media / Narrative | 3 |
| Organization / Resource | 4 |
| Ideology / Identity | 1 |
| Constitutional / Power Move | 1 |
| Total | 31 |

Note: Opposition currently totals 31. Before final implementation, remove or merge one card. Recommended cut: reduce either Media / Narrative from 3 to 2 or Organization / Resource from 4 to 3.

## 15. Required Card Metadata

All cards should use a consistent metadata structure.

```yaml
id: expose_teacher_admission_scam
name: Expose Teacher Admission Scam
category: scandal_accusation
role_allowed: ["opposition"]
cost: 14

target:
  government: true
  opposition: true
  public: true

effects:
  scheduled:
    - label: first_public_reaction
      timing:
        min_turns: 1
        max_turns: 1
      visible: true
      effects:
        government:
          coins: 0
          party_morale: -1
          corruption_score: 4
          media_image: -3
          public_support: -1
        opposition:
          coins: -14
          party_morale: 2
          corruption_score: 0
          media_image: 2
          public_support: 1
        public:
          undecided_support: 0
          public_mood: -1

    - label: scandal_resolution
      timing:
        min_turns: 2
        max_turns: 5
      visible: true
      chance_table:
        proven_true:
          weight: 25
          effects:
            government:
              party_morale: -4
              corruption_score: 8
              media_image: -6
              public_support: -5
            opposition:
              party_morale: 3
              media_image: 4
              public_support: 4
        partly_true:
          weight: 25
          effects:
            government:
              party_morale: -2
              corruption_score: 4
              media_image: -3
              public_support: -2
            opposition:
              media_image: 2
              public_support: 2
        unclear:
          weight: 30
          effects:
            government:
              media_image: -1
              corruption_score: 1
            opposition:
              media_image: 1
        proven_false:
          weight: 20
          effects:
            government:
              party_morale: 2
              corruption_score: -2
              media_image: 3
              public_support: 3
            opposition:
              party_morale: -4
              media_image: -5
              public_support: -5

hidden_effects:
  scheduled:
    - label: public_memory_shift
      timing:
        min_turns: 1
        max_turns: 3
      visible: false
      effects:
        public_memory:
          scandal_fatigue: 1
          corruption_suspicion_government: 3

risk_roll:
  chance: 20
  bad_outcome: "Accusation is seen as politically motivated."
  effects:
    opposition:
      party_morale: -2
      media_image: -2
      public_support: -1

ideology_tags:
  strong_fit: ["anti_corruption"]
  weak_fit: ["development_first"]
```

Effect values are deltas. Positive values increase a stat; negative values decrease it.

## 16. Scandal And Counter System

Scandal cards should not always stick.

Opposition has more scandal cards because the government has more power, more accountability, and more chances for corruption exposure.

### Scandal Outcome Types

| Outcome | Meaning |
|---|---|
| Proven True | Target takes major damage; accuser gains credibility |
| Partly True | Target takes moderate damage; accuser gains some credibility |
| Unclear | Small media damage; suspicion may remain |
| Proven False | Accuser is punished; target may recover |

### Opposition Scandal Base Weights

| Outcome | Weight |
|---|---:|
| Proven True | 25 |
| Partly True | 25 |
| Unclear | 30 |
| Proven False | 20 |

### Government Scandal Base Weights

| Outcome | Weight |
|---|---:|
| Proven True | 30 |
| Partly True | 25 |
| Unclear | 25 |
| Proven False | 20 |

Government scandals may be somewhat better sourced due to administrative access, but public may suspect misuse of power.

### Defensive Counter Cards

After a scandal card is played, the target party may use a defensive/counter card on the next turn.

Counter cards may:

- Reduce scandal damage.
- Shift the chance table.
- Increase chance of unclear/proven false outcomes.
- Protect media image.
- Recover party morale.

Counter cards should not fully erase reality. If a scandal is true, defense can reduce damage but should not make it harmless.

Example counter cards:

- Deny Allegation
- Order Independent Inquiry
- Release Documents
- Sacrifice Minister / Leader
- Attack Accuser Credibility
- Media Defense Campaign
- Legal Notice
- Fact-Check Campaign
- Apology And Correction
- Change The Narrative

## 17. News System

Each turn has two news items.

### External News

External news is inspired by the in-game month and broader real-world-style conditions, but should remain fictionalized.

Examples:

- Fuel prices rise.
- Unemployment concerns increase.
- Exam paper leak allegations spread.
- Floods damage rural areas.
- Farmers demand relief.
- Student groups protest fee hikes.
- Health system faces pressure.
- Local industry slows down.

### Internal News

Internal news is generated from game state and last-turn events.

Examples:

- New government formed by party.
- Scandal allegation dominates debate.
- Student movement gains attention.
- Government announces new welfare push.
- Opposition yatra gets strong turnout.
- Public questions party funding.

On the first turn of a new cycle, internal news should be:

```text
New government formed by [Party Name].
```

## 18. News Reaction Metadata

Each news item has 4 reaction options.

Each reaction affects:

- Player party morale.
- Player corruption score.
- Player media image.
- Player public support.

News reactions may also affect hidden public memory and issue salience.

```yaml
id: fuel_price_rise_oct_2020
type: external
title: Fuel Prices Rise Across The State
month_tags: ["october", "november"]
issue_tags: ["inflation", "economy", "transport"]
description: "Rising fuel costs are increasing pressure on households and small businesses."

reaction_options:
  - id: blame_government
    text: "Blame the government for poor price control."
    role_allowed: ["opposition"]
    effects:
      player_party:
        party_morale: 2
        corruption_score: 0
        media_image: 1
        public_support: 2
    hidden_effects:
      public_memory:
        economic_attack_pattern: 1
        inflation_issue_salience: 2
    risk:
      chance: 20
      bad_outcome: "Public sees it as routine blame politics."
      effects:
        player_party:
          media_image: -2
          public_support: -1

  - id: promise_subsidy
    text: "Promise targeted subsidy for transport workers."
    role_allowed: ["government", "opposition"]
    effects:
      player_party:
        party_morale: 1
        corruption_score: 0
        media_image: 2
        public_support: 2

  - id: demand_inquiry
    text: "Demand inquiry into fuel tax collection."
    role_allowed: ["opposition"]
    effects:
      player_party:
        party_morale: 1
        corruption_score: 0
        media_image: 1
        public_support: 1

  - id: stay_silent
    text: "Avoid reacting for now."
    role_allowed: ["government", "opposition"]
    effects:
      player_party:
        party_morale: -1
        corruption_score: 0
        media_image: -1
        public_support: 0
```

## 19. Strategic / Special Actions

Special actions are not cards. The player chooses one special action each turn after news reactions and main card play.

### MVP Special Action List

| # | Special Action | Role | Purpose |
|---|---|---|---|
| 1 | Conduct Opinion Poll | Govt + Opposition | Reveal public support, mood, top issues, hidden memory hints |
| 2 | Media Campaign | Govt + Opposition | Improve media image and slightly influence public support |
| 3 | Investigate Active Scandal | Govt + Opposition | Improve chance that a scandal resolves in your favor |
| 4 | Coalition Talk | Govt + Opposition | Build support with smaller parties/independents before election |
| 5 | No-Confidence Motion | Opposition only | Try to collapse weak government and trigger early election |
| 6 | Internal Party Meeting | Govt + Opposition | Restore morale and reduce internal damage |
| 7 | Fundraising Drive | Govt + Opposition | Gain coins, with corruption/media risk |
| 8 | Election Preparation | Govt + Opposition | Improve election performance and government formation chance |
| 9 | Damage Control | Govt + Opposition | Reduce impact of negative media/scandal/public backlash |
| 10 | Volunteer Mobilization | Govt + Opposition | Boost cadre strength and improve service/agitation cards |



### Special Action Metadata

```yaml
id: conduct_opinion_poll
name: Conduct Opinion Poll
category: information
role_allowed: ["government", "opposition"]
cost: 8
availability:
  type: always
effects:
  scheduled:
    - label: poll_report
      timing:
        min_turns: 1
        max_turns: 1
      visible: true
      effects:
        self_party:
          coins: -8
          party_morale: 0
          corruption_score: 0
          media_image: 0
      reveal:
        public_support_accuracy: high
        public_mood: true
        top_issues: true
        hidden_memory_hint: true
risk_roll:
  chance: 10
  bad_outcome: "Poll sample is misleading."
```

## 20. No-Confidence Mechanic

No-confidence is a special action available only to the opposition.

Unlock conditions:

- Government public support is below 30%.
- Government party morale is low.

Suggested morale threshold:

- Government party morale below 35.

Outcome depends on:

- Public mood.
- Government morale.
- Opposition media image.
- Opposition trust.
- Recent scandal history.
- Coalition readiness.

Success:

- Government falls.
- Early election is called.

Failure:

- Opposition morale drops.
- Opposition media image drops.
- Government morale rises.
- Government public support may recover slightly.
- No-confidence enters cooldown.

## 21. Coalition And Government Formation

Elections are based on vote share in the MVP.

After election:

- Party with stronger election result forms government.
- If results are close, coalition readiness can influence government formation.
- Coalition talk before election improves coalition readiness.
- Each election is expensive. After an election, each party loses 70% of its current coins.

Coalition partners are abstracted in MVP as smaller parties/independents rather than fully simulated parties.

## 22. Election Model

MVP election model is vote-share based, inspired by Indian state elections.

Inputs:

- Government public support.
- Opposition public support.
- Undecided support.
- Media image.
- Party morale.
- Coins.
- Coalition readiness.
- Anti-incumbency.
- Public memory.
- Election preparation.

Outputs:

- Vote share.
- Government formation result.
- New role assignment.
- Election spending result: each party keeps only 30% of its pre-election coins.

Future versions may add:

- Constituencies.
- Seat conversion.
- Regions.
- Caste/community blocs.
- Turnout.
- Swing seats.

## 23. Starting Scenarios

MVP scenarios may include:

### Strong Majority Government

Government starts strong.

- High coins.
- High morale.
- High media image.
- High public support.
- Opposition starts weaker.

### Weak Coalition Government

Balanced starting values.

- Medium government support.
- Lower morale.
- Higher instability.
- No-confidence may become possible earlier.

### Historical-Inspired State Campaign

Example inspiration:

- Long incumbency.
- Rising opposition momentum.
- Youth unrest.
- Anti-incumbency wave.

All scenarios should be fictionalized.

## 24. Required First Deck Cards Mentioned So Far

Cards to include when finalizing deck lists:

### Positive / Service

- Cleanliness Drive
- Blood Donation Camp
- Unity March
- Relief Work During Crisis
- Free Legal Aid Camp
- Job Help Camp
- Community Kitchen
- Public Listening Sabha
- Volunteer Health Camp
- Interfaith Harmony Meet

### Organization / Resource

- Strengthen Party Base
- Organize Fundraiser
- Cadre Training Camp
- Build Booth Network
- Membership Drive
- Local Body Push

### Scandal Examples

- Expose Teacher Admission Scam
- Expose Local Corruption
- Demand Inquiry Into Fuel Tax
- Investigate Opposition Funding
- Expose Policy Failure

### Government Governance Examples

- Launch Welfare Scheme
- Announce Infrastructure Project
- Law And Order Drive
- Farmer Loan Relief
- Youth Employment Mission
- Women Safety Campaign
- Subsidy Announcement
- Education Reform Bill
- Disaster Relief Package
- Digital Governance Portal

## 25. Open Design Items

These should be finalized before implementation:

- Final 30-card government deck.
- Final 30-card opposition deck.
- Opposition deck currently totals 31 by category distribution, so one card/category count must be reduced.
- Exact starting stats for each scenario.
- Exact stat caps and clamping rules.
- Exact election formula.
- Exact AI decision logic.
- Exact hidden public memory fields.
- Exact list of external news events by month.
- Whether public support must always total 100 including undecided.
- Whether coins reaching exactly 0 ends the game immediately or after the turn resolves.
