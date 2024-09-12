# Person-Hours

## Estimates

(Some estimates are negligible or were already completed when estimation was done). For posterity this info is maintained here:

Estimate by task:
1. Game Setup (N/A rough implementation by Kyler, restructure into classes for modularity ~3hr)
2. Playing the Game (est. 2.5-3 hours)
  - Have to test and ensure robust behavior. Could encounter unexpected issues or refactoring required to support
    manipulating initial game state
3. Destroying a Ship (est. <1 hour)
  - Should not take too long if modularity was correctly set up, simply check if a ship has no health points (or has been hit in every position)
4. Player's View (est. <1 hour)
  - given that the board state should be stored in a format for easy manipulating (for playing), it is likely already stored in an easy state for easy display
5. Game End (est. <1 hour)
  - given that most logic should be implemented this should be as simple as checking if all a players ships are destroyed


## Actual
This table makes no attempt to track where/when work was done. Use `git` to see history/location of work.

| Person   | Hours |
| -------- | ----- |
| Kyler    | 5     |
| Cody     | 0     |
| Joon     | 0     |
| Hayden   | 0     |
| Harrison | 0     |