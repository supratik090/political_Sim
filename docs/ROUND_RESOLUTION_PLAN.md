# Round Resolution Plan

## Goal

Each monthly turn should behave like a round where every human/computer party submits choices before the round resolves.

## Turn Flow

1. Show current scenario, date, public mood, party metrics, news, and cards.
2. Current player selects one card.
3. Current player selects reactions for news items.
4. Current player locks choices.
5. If another human player still needs to play, pass control to that player.
6. Computer parties choose cards and news reactions automatically.
7. Once all parties have submitted, resolve the round.
8. Show round summary before the next month begins.

## GameService Steps For Next Turn

When `Next Turn` is selected:

1. Validate current player has selected a card.
2. Validate current player has selected news reactions.
3. Store the player's pending turn submission.
4. Check whether all human players have submitted.
5. If not all humans are done, return the same month with `activeHumanPlayerIndex + 1`.
6. If all humans are done, generate computer submissions.
7. Resolve every submitted card.
8. Resolve every submitted news reaction.
9. Add 0-10 coins to each party based on news reaction quality, public fit, and risk.
10. Apply card effects to self party, opponent party, public support, and hidden memory.
11. Apply news reaction effects to each party.
12. Clamp metrics to allowed ranges.
13. Create round commentary.
14. Store cards played by all parties in last round.
15. Store metric deltas for every party.
16. Advance date by one month.
17. Reset active player/submissions for the new month.

## Round Summary Output

The turn view should include:

- Cards played by all parties last round.
- News reactions chosen by all parties.
- Coins gained from news reactions.
- Metric deltas per party.
- Commentary for card outcomes.
- Commentary for news reaction outcomes.
- Significant score movement callouts.

## Metric Delta Display

For each party, every visible metric should include:

- Current value.
- Delta from previous round.
- Green for positive movement.
- Red for negative movement.

Special case:

- `corruptionScore` is bad when it increases, so its color should be inverted.

## Card Use Tracking

Each card has `maxUsesPerCycle`.

During a cycle:

- Selecting a card temporarily reduces available uses in the UI.
- Canceling restores the available use.
- Locking/advancing stores the use permanently for that cycle.

Current UI behavior:

- Selected card appears top-right using the same category color.
- Deck shows available count reduced by 1 while selected.
- Canceling card selection restores the displayed count.
