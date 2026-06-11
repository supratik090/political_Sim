# Admin Content Architecture

## Goal

The admin screen maintains scenario rules, cards, and news in MongoDB through the Spring Boot backend.

The first scenario target is:

```text
west_bengal_2000
West Bengal 2000
```

The scenario is fictionalized for gameplay, using animal party names and invented state/party names.

MVP scenarios support exactly three political parties:

- One starts as `GOVERNMENT`.
- One starts as `OPPOSITION`.
- One starts as `THIRD_PARTY`.

Each party has a controller type:

- `HUMAN`
- `COMPUTER`

Allowed game setups:

- 1 human + 2 computer
- 2 human + 1 computer

The admin UI stores parties in `politicalParties` while also maintaining compatibility fields such as `governmentPartyName`, `oppositionPartyName`, `thirdPartyName`, and their starting stats.

## Mongo Collections

```text
scenario_definitions
card_definitions
news_definitions
```

## Admin API

```text
GET    /api/admin/scenarios
POST   /api/admin/scenarios
GET    /api/admin/scenarios/{id}
PUT    /api/admin/scenarios/{id}
DELETE /api/admin/scenarios/{id}

GET    /api/admin/cards?scenarioKey=west_bengal_2000
POST   /api/admin/cards
GET    /api/admin/cards/{id}
PUT    /api/admin/cards/{id}
DELETE /api/admin/cards/{id}

GET    /api/admin/news?scenarioKey=west_bengal_2000
POST   /api/admin/news
GET    /api/admin/news/{id}
PUT    /api/admin/news/{id}
DELETE /api/admin/news/{id}
```

## Design Choice

The Java models keep searchable fields typed, but effect/rule fields flexible:

- `target`
- `visibleEffects`
- `hiddenEffects`
- `riskRoll`
- `ideologyTags`
- `timing`
- `ruleWeights`
- `reactionOptions`
- `weights`

This lets us tune cards, news, reactions, and balancing weights from MongoDB without rebuilding Java classes every time a rule changes.

Cards and news both support weights:

- Card weights live in `card_definitions.weights`.
- News selection weights live in `news_definitions.weights`.
- News reaction weights live per item in `news_definitions.reactionOptions[].weight`.

Cards also support `maxUsesPerCycle`.

For the MVP deck:

- Each party has 30 card definitions.
- Each card can be used twice per 60-month cycle.
- This gives each party 60 total card uses per cycle.

The admin UI provides quick-delete selectors for Cards and News, plus the existing JSON edit/delete controls.

## Python UI

The Streamlit app has two modes:

- `Game`
- `Admin`

Admin mode includes tabs for:

- Scenarios
- Cards
- News

Each tab supports create, read, edit, and delete through the backend API.
