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
-- Team 4 --
6. AI Opponent (est. 6.5 hours)
7. Custom Feature - Sound Effects (est. 2 hours)
8. Extra Game Setup (est. ~ 2.5 hours)


## Actual
This table makes no attempt to track where/when work was done, it is simply the cumulative result of Person-Hours.

- The project rubric makes a point of saying
> This needs to be a day-by-day accounting from each team member on how many hours they spent on the project, including team and GTA meetings, coding, testing, documenting, etc

Ok, well git does that, here: [file history](https://github.com/Tyler51235/EECS-581/commits/main/Documentation/Person-Hours.md)

| Person   | Hours |
| -------- | ----- |
| Kyler    | 5.5   |
| Cody     | 4.5   |
| Joon     | 2.0   |
| Hayden   | 1.5   |
| Harrison | 3.0   |
------ Team 4 ------
| Ethan    | 2.5   |
| Tanner   | 2.0   |
| Edgar    | 1.0   |
| Gavin    | 2.25  |
| Mario    | 2.0   |

All:
    Thursday 09/26 - 15 mins (GTA team meeting)
    Thursday 09/26 - 10 mins (team meeting)

Ethan:
    Wednesday 09/25 - 30 mins (design AIOpponent class)
    Thursday 09/26 - 1 hr (start medium_shot and helper methods)
    Friday 09/27 - 1hr (finish medium_shot algorithm)

Gavin:
    Wednesday 09/25 - 2 hrs (update play function in Battleship.py and create aiPlaceShips function in Grid.py)
    Thursday 09/26 - 15 min (Redo some code in play function and aiPlaceShips)

Edgar:
    Thursday 09/26 - 30 min (start easy_shot and start and finish hard_shot)
    Sunday 09/29 - 30 min (finish easy shot)
