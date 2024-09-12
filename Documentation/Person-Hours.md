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
This table makes no attempt to track where/when work was done, it is simply the cumulative result of Person-Hours.

- The project rubric makes a point of saying
> This needs to be a day-by-day accounting from each team member on how many hours they spent on the project, including team and GTA meetings, coding, testing, documenting, etc

Ok, well git does that, here: [file history](https://github.com/Tyler51235/EECS-581/commits/main/Documentation/Person-Hours.md)

| Person   | Hours |
| -------- | ----- |
| Kyler    | 5     |
| Cody     | 3     |
| Joon     | 0     |
| Hayden   | 0     |
| Harrison | 0     |