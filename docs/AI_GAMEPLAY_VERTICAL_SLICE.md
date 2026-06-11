# AI Gameplay Vertical Slice

## Current Slice

Computer-controlled parties now submit a full monthly move after all human players have locked their choices.

The AI chooses:

- one legal party card for its current role
- one legal reaction for each active monthly news item
- a default response placeholder for generated last-turn news

Each AI party also has a tunable `aiProfile` that can be stored on scenario party definitions and copied into active game state.

```json
{
  "style": "AGGRESSIVE_POPULIST",
  "riskTolerance": 0.7,
  "scandalPreference": 0.8,
  "welfarePreference": 0.5,
  "coalitionPreference": 0.4,
  "mediaPreference": 0.65,
  "ideologyStrictness": 0.75,
  "intentThresholds": {
    "governmentNoConfidenceSupport": 30.0,
    "lowCoins": 65.0,
    "corruptionCrisis": 48.0
  },
  "scoringWeights": {
    "selfPublicSupport": 4.0,
    "intentFit": 8.0,
    "categoryPreference": 5.0
  },
  "categoryPreferences": {
    "scandal_accusation": 0.95,
    "agitation_movement": 0.8,
    "media_narrative": 0.75
  }
}
```

The scalar fields are the friendly personality controls. The map fields are the admin/balancing controls and should live in Mongo with scenario party definitions.

## Intent Selection

Before scoring cards, the AI chooses one strategic intent for the month:

- `GAIN_SUPPORT`
- `RESTORE_MORALE`
- `ATTACK_RIVAL`
- `DEFEND_IMAGE`
- `RAISE_FUNDS`
- `PREPARE_ELECTION`
- `FORCE_NO_CONFIDENCE`
- `SURVIVE_SCANDAL`

Intent is selected from current stats, opponent weakness, government vulnerability, election timing, and party AI profile.

## Card Selection Heuristic

The AI scores every active card allowed for its role and chooses the highest score.

The score currently considers:

- card metadata weights: `basePlayWeight`, `aiPriorityWeight`, `publicImpactWeight`, `riskWeight`
- selected monthly intent
- AI profile preferences: risk, scandal, welfare/service, media, ideology strictness
- self effects: public support, media image, party morale, corruption, coins
- opponent effects: public support, media image, corruption
- affordability based on current coins and card cost
- role fit: government prefers governance/defense, opposition and third party prefer scandal/agitation/service
- tactical needs: low morale, weak media image, low public support, high corruption, low coins
- ideology fit against card `ideologyTags`
- election timing pressure

## News Reaction Heuristic

The AI scores all role-allowed reactions for each news item.

The score currently considers:

- reaction weight
- public support, media image, party morale, corruption, and coin effects
- current party weakness, so a struggling party values recovery effects more
- risk chance penalty

## Next Improvements

- Track card usage on the backend so AI cannot exceed each card's `maxUsesPerCycle`.
- Use hidden public memory when it is implemented, so AI can respond to long-term voter fatigue and trust.
- Add no-confidence and coalition action selection once special actions move into backend resolution.
- Make generated-news reactions real content definitions instead of the current placeholder key.
- Add AI memory for repeated categories, rival history, and public fatigue.
