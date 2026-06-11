# Sprint 1 Architecture

## Goal

Create the smallest playable/testable vertical slice:

- Spring Boot backend.
- MongoDB-backed game sessions.
- Python Streamlit test UI.
- Create game and view current turn state.

## Current Backend Modules

```text
backend/src/main/java/com/politicalsim/
  api/          REST request/response models and controllers
  game/         game session persistence and turn-view service
  party/        party roles, ideology, party state, party stats
  publicmood/   visible public state
```

## Current API

```text
POST /api/games
GET  /api/games/{gameId}
GET  /api/games/{gameId}/turn-view
```

## Create Game Request

```json
{
  "playerPartyName": "Elephant Congress",
  "playerRole": "OPPOSITION",
  "ideology": "ANTI_CORRUPTION",
  "stateName": "Dakshin Pradesh",
  "startDate": "2020-10-01"
}
```

## Turn View Purpose

`GET /api/games/{gameId}/turn-view` is the main UI endpoint. The Python UI should stay dumb and render this response without owning gameplay logic.

The endpoint returns:

- Current turn/date/cycle status.
- Government party health.
- Opposition party health.
- Third party health.
- Which party is player-controlled.
- Public mood.
- No-confidence availability.
- Pending and last results.

## Next Backend Modules

Add these in later sprints:

```text
card/       Card definitions, card service, card resolver
news/       News definitions, reaction resolver
action/     Special action definitions and resolver
effect/     Shared scheduled effect engine
election/   Election and government formation
ai/         AI choices
content/    MongoDB-backed editable rules/content loaders
```

## Important Rule

Cards, news reactions, and special actions should all use one shared effect engine. Do not hardcode individual card behavior in Java services.

## Three-Player Rule

Games now support exactly three parties:

- Government
- Opposition
- Third Party

Controller mix must be either:

- 1 human + 2 computer
- 2 human + 1 computer
