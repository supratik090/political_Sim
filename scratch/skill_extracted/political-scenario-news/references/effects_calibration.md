# Calibrating Effects, Hidden Effects, and Risk

All numbers below are integers. `playerParty` effects are bounded **-10..10**. Don't
default to the same values every time — vary magnitude with how big a deal the news
item is, and vary sign/size across the four reactions so choices feel meaningfully
different.

## 1. Severity tiers (set the overall scale for an item)

Look at the item's `issueTags`/`reactionProfile` and pick a tier before writing any
numbers:

| Tier | Example issues | Base effect magnitude (the "good" outcome) | Risk chance | Risk penalty magnitude |
|---|---|---|---|---|
| **Routine/ceremonial** | cultural events, pilgrimages, minor inaugurations | 1-3 | 5-10% | 1-2 |
| **Standard governance** | ordinary policy news, land approvals, bank/economy stories | 2-4 | 10-15% | 1-3 |
| **High-salience** | rural distress, statehood/identity politics, big protests | 3-6 | 12-18% | 2-4 |
| **Crisis** | security incidents, deaths, major scandals | 4-10 | 15-25% | 3-6 |

Use the top of a tier's range for `opp_demands`/`gov_action` (the "doing something"
options) and the bottom of the range for `joint_forum` (steadier, lower-variance).

## 2. Sign conventions per reaction

- **`gov_action`** (GOVERNMENT only): positive `partyMorale`, `mediaImage`,
  `publicSupport` for the government party at roughly tier magnitude;
  `corruptionScore` usually `0` (occasionally slightly positive if the action
  itself looks like patronage, e.g. `+1`). Risk block: administrative/execution
  failure, moderate penalty.
- **`opp_demands`** (OPPOSITION + THIRD_PARTY): positive `partyMorale`,
  `mediaImage`, `publicSupport` for whichever non-government party picks it, at or
  slightly above `gov_action` magnitude (opposition benefits more from visible
  pressure than government does from routine governance). `corruptionScore` `0`.
  Risk block: looks like partisan grandstanding, moderate penalty on `publicSupport`
  and `mediaImage`.
- **`joint_forum`** (all roles): moderate positive across the board, but
  **`corruptionScore` should be slightly negative** (e.g. `-1`) — consensus-building
  is coded as clean governance. Lower risk chance than the other two active options;
  penalty is "radical/fringe actors refuse to cooperate."
- **`no_comment`** (all roles): always net negative — `partyMorale`, `mediaImage`,
  `publicSupport` all negative (roughly `-2` to `-4` for standard items, more for
  crisis items), `corruptionScore` slightly positive (`+1`) since disengagement
  reads as "nothing to see here." `risk` is usually `{}` since there's no active
  action to fail — the penalty is already baked into the base effect.

## 3. Hidden effects (`publicMemory`)

`publicMemory` keys represent slow-building sentiment that can be referenced by
later events in the same scenario (the game engine can look these up). Conventions:

- Pick 2-4 memory keys per scenario and reuse them across every item that shares a
  theme, e.g. `apStabilityMemory` (general governance trust), `ruralTrustMemory`
  (farmer/rural sentiment), `corruptionMemory` (accumulated graft perception),
  `identityMemory` (statehood/regional-identity pressure).
- Typical values: `-3..3`. `no_comment` commonly *adds* to a negative memory (e.g.
  `apStabilityMemory: 2` where positive means "growing instability," as in the
  sample file) even though its immediate effects are also negative — memory and
  immediate effects don't have to share a sign convention, but be internally
  consistent about what "positive" means for each named key across the whole file.
- It's fine for a reaction to have `"publicMemory": {}` — not every choice needs to
  leave a durable trace. `gov_action` and `joint_forum` on high-salience/crisis
  items almost always should have one, though.

## 4. Risk blocks

- `chance` scales with tier (table above) — don't make every item's risk chance
  identical; vary ±5 points item to item to avoid a mechanical feel.
- `badOutcome` should name a *specific* failure mode for that action, not a generic
  "something goes wrong" — e.g. "Contractors miss the deadline, drawing local
  ridicule" rather than "The plan fails."
- The `effects` inside `risk` fire *in addition to* the base `effects` when the roll
  hits — so they should be smaller in magnitude than the base effect and always net
  negative, even when the base effect for that reaction was positive.
- `no_comment` normally has `"risk": {}` (no separate roll — see §2).

## 5. Weight field

`weight` controls how often the engine surfaces an option relative to the others in
the same news item (not a game-score value). Keep `gov_action`/`opp_demands` around
`1.1-1.3`, `joint_forum` around `1.0-1.15`, and `no_comment` low, around `0.2`,
matching the sample file. Don't tie `weight` to how "good" the option is — it's about
frequency of appearing as a choice, not payoff.

## 6. Sanity checklist before validating

- [ ] Every `playerParty` value is an integer in -10..10.
- [ ] `no_comment` effects are net negative on morale/media/support.
- [ ] Risk `chance` is 0-100 and scales with severity tier.
- [ ] Magnitudes vary across items — a crisis item should clearly hit harder than a
      ceremonial one.
- [ ] The same `publicMemory` keys are reused consistently within a scenario, not
      invented fresh per item.
