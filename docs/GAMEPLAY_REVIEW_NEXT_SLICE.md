# Gameplay Review: Public Support And Surprise

## Problems Found

- Public support was being added like a normal stat, so vote share could grow unrealistically.
- Undecided voters were too easy to capture because every positive public effect immediately became support.
- Party support plus undecided support could exceed 100% in scenario setup.
- Card risk metadata existed, but round resolution did not apply those surprise outcomes.
- Gameplay felt predictable because most actions were direct visible point changes.

## Implemented Slice

- Public support effects are now treated as support pressure, not direct vote share.
- At round end, negative pressure can move voters from a party into undecided.
- Positive pressure can only convert a dampened amount of undecided support.
- Party support plus undecided support is normalized to 100%.
- Scenario creation now normalizes the starting public support pool.
- Card and news reaction risk rolls now apply their configured bad-outcome effects.
- Round commentary now reports voter movement and surprise backlash events.

## Current Model

Public support movement is deliberately slow:

- pressure of `+1` or `+2` usually does not move actual vote share
- stronger positive pressure can convert up to `2%` undecided voters in a round
- negative pressure can release up to `3%` support into undecided voters
- support cannot appear from nowhere
- undecided voters act as a buffer, not a free pool to harvest every month

## Recommended Next Slice

- Move public support dampening values into scenario rule weights.
- Add hidden public memory so repeated scandals/protests/services alter future conversion rates.
- Add poll accuracy and survey narrative so the player sees signals, not perfect truth.
- Add delayed effects queue so some card outcomes reveal after 1-5 turns.
- Add player-facing risk hints such as low/medium/high instead of exact risk percentages.
