# Scenario News JSON Schema

This is the exact structure to produce. Field names, nesting, and types matter —
the game engine parses this directly.

## Top level

```json
{
  "reviewStatus": "draft",
  "scenarioKey": "andhra_pradesh_2001",
  "period": {
    "startMonth": "2001-01",
    "endMonth": "2005-12",
    "months": 60
  },
  "sourceNotes": "One-line note on what this scenario covers and how it was built.",
  "defaults": {
    "weights": {
      "baseSelectionWeight": 1.0,
      "reactionProfile": "default"
    }
  },
  "newsItems": [ /* see below */ ]
}
```

- `reviewStatus`: `"draft"` unless the user explicitly asks you to mark it approved.
- `scenarioKey`: snake_case, matches the filename prefix.
- `period.months`: must equal the number of calendar months from `startMonth` to
  `endMonth` inclusive, and should equal `len(newsItems)` if you're doing one item per
  month (the normal case).
- `defaults`: leave as shown unless the user asks for different global defaults.

## Each entry in `newsItems`

```json
{
  "newsKey": "ap2001_2001_01_cyberabad_it",
  "month": "2001-01",
  "title": "Cyberabad Tech Hub Phase 1 Inaugurated in Hyderabad (2001-01)",
  "description": "Two sentences: what happened, and why it matters politically.",
  "issueTags": ["infrastructure"],
  "weights": {
    "baseSelectionWeight": 1.15,
    "reactionProfile": "governance"
  },
  "reactionOptions": [ /* exactly 4 — see below */ ],
  "type": "external",
  "monthTags": ["2001-01"],
  "crisisTriggerKey": null,
  "crisisDuration": 2
}
```

- `newsKey`: unique across the whole file. Pattern:
  `{scenarioShortCode}_{yyyy}_{mm}_{issue_slug}`. Keep `scenarioShortCode` short and
  consistent (the sample uses `ap2001` for `andhra_pradesh_2001`).
- `month` / `monthTags`: both set to the same `"YYYY-MM"`, and must fall inside
  `period.startMonth`..`period.endMonth`.
- `issueTags`: controlled vocabulary — reuse across the file. Suggested set (extend as
  needed for the state/period, but keep it a small reused set, not one-off tags):
  `politics`, `rural`, `protest`, `land_rights`, `security_crisis`, `infrastructure`,
  `economy`, `corruption`, `identity`, `governance`.
- `weights.reactionProfile`: groups items that should feel similar in tone/response
  (e.g. `politics`, `land_rights`, `security_crisis`, `governance`). Reuse these labels.
- `type`: `"external"` for normal one-off/recurring news. Only use `"crisis"` if this
  item is meant to spin up a persistent crisis state — in that case set
  `crisisTriggerKey` to a non-null key and `crisisDuration` to how many months it
  persists (>2). Otherwise `crisisTriggerKey` is always `null` and `crisisDuration`
  stays at its default (`2`) even though it's unused for `"external"` items.

## Each entry in `reactionOptions` (exactly 4, in this order)

```json
{
  "reactionKey": "ap2001_2001_01_cyberabad_it__gov_action_cyberabad_it",
  "text": "Inaugurate the tech park and announce tax breaks for anchor tenants.",
  "roleAllowed": ["GOVERNMENT"],
  "effects": {
    "playerParty": {
      "partyMorale": 2,
      "corruptionScore": 0,
      "mediaImage": 3,
      "publicSupport": 3
    }
  },
  "hiddenEffects": {
    "publicMemory": {
      "apStabilityMemory": 1
    }
  },
  "risk": {
    "chance": 15,
    "badOutcome": "Administrative delays stall the commission, drawing minor local criticism.",
    "effects": {
      "playerParty": {
        "partyMorale": -1,
        "corruptionScore": 0,
        "mediaImage": -1,
        "publicSupport": -2
      }
    }
  },
  "weight": 1.2
}
```

- `reactionKey`: `{newsKey}__{suffix}` where suffix is one of `gov_action_{slug}`,
  `opp_demands_{slug}`, `joint_forum_{slug}`, `no_comment` (no slug needed for
  `no_comment` — keep it literally `"no_comment"` to match the sample, or
  `no_comment_{slug}`, either is fine as long as it's consistent within the file).
- `roleAllowed`: see the table in SKILL.md Step 3. Always exactly these three
  patterns plus the shared no_comment pattern — don't invent new role combinations.
- `effects.playerParty`: all four sub-fields always present, integers in **-10..10**
  (0 allowed). See `effects_calibration.md` for how to size these.
- `hiddenEffects.publicMemory`: an object with zero or more scenario-specific keys →
  small integers (typically -3..3). Can be `{}` if this reaction has no durable
  memory effect (this is common for `no_comment`, uncommon for the other three).
- `risk`: either `{}` (no risk — typical for `no_comment`) or a full block with:
  - `chance`: integer 0-100 (percent chance the bad outcome fires).
  - `badOutcome`: one sentence describing what goes wrong.
  - `effects.playerParty`: same shape as above, values usually smaller-magnitude
    negatives than the base effect (this is what fires *on top of* the base effect
    when the risk triggers — the game engine applies base effects unconditionally
    and risk effects only on the roll).
- `weight`: float, relative selection weight among the 4 options when the engine
  offers a hand of choices. `no_comment` should always be the lowest (~0.2). The
  other three are typically 1.0-1.3.
