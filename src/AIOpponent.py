"""
Contains the AI Opponent class

- Input an opponent's grid
- Shot methods return coordinates 

Authors: Ethan Wheat 
Date: 2024-09-25
"""
from src.Grid import Grid

class AIOpponent:
    def __init__(self, grid: Grid) -> None:
        self.opponent_grid = grid  # the grid object of the opponent

        self.rows = grid.rows  # number of rows
        self.cols = grid.cols  # number of columns

        # list of ship positions in (row, col) format
        self.positions = [pos for ship in grid.ships for pos in ship.positions()]

    def easy_shot(self) -> tuple[int, int]:  # returns a random coordinate of a valid shot
        return (0,0)    

    def medium_shot(self) -> tuple[int, int]:  # returns a random coordinate of a valid shot until hit
                                               # then returns orthogonally adjacent coords until sunk
        return (0,0)

    def hard_shot(self) -> tuple[int, int]:  # returns coordinate that is guaranteed to be a hit
        return (0,0)
