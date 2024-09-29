"""
Contains the AI Opponent class

- Input an opponent's grid
- Shot methods return coordinates 

Authors: Ethan Wheat, Edgar Mendez 
Date: 2024-09-25
"""
from src.Grid import Grid
import random

class AIOpponent:
    def __init__(self, grid: Grid) -> None:
        self.opponent_grid = grid  # the grid object of the opponent

        self.rows = grid.rows  # number of rows
        self.cols = grid.cols  # number of columns
        self.shot_grid = [[0 for _ in range(self.rows)] for _ in range(self.cols)]  # used for tracking shots

        # list of ship positions in (row, col) format
        self.positions = [pos for ship in grid.ships for pos in ship.positions()]
        
        # trackers for medium level AI self
        self.current_hits = []  # tracks the hits on a current ship
        self.targets = []  # tracks orthogonal/valid next targets
        self.hit_backlog = []  # if another boat struck orthogonally, add to backlog

    def easy_shot(self) -> tuple[int, int]:  # returns a random coordinate of a valid shot
        row, col = random.randint(0,9), random.randint(0,9)
        while self.valid_shot(row, col) != True:
            row, col = random.randint(0,9), random.randint(0,9)
        return (row, col)
        
    def medium_shot(self) -> tuple[int, int]:  # returns a random coordinate of a valid shot until hit
                                               # then returns orthogonally adjacent coords until sunk
        if len(self.current_hits) == 0: # random fire
            while True:
                row = random.randint(0, self.rows - 1)  # retrive a random row
                col = random.randint(0, self.cols - 1)  # retrieve a random col
                if self.shot_grid[row][col] == 0:  # valid shot that has not been done yet
                    if (row, col) in self.positions:  # if shot would be a hit 
                        if self.would_sink(row, col) == False:  # check if the shot would not sink a ship (1 length ship)
                            self.shot_grid[row][col] = 2  # mark the spot as hit
                            self.current_hits.append((row, col))  # update the current hits of a ship
                            self.targets = self.next_targets()  # populate adjacent targets
                    else:  # if a shot would be a miss
                        self.shot_grid[row][col] = 1  # mark the spot as a miss
                    return (row,col)  # return the shot coordinates

        else:  # orthogonally fire
            pos = random.choice(self.targets)  # choose a random option from the targets
            self.targets.remove(pos)  # remove that option
            row, col = pos  # retrieve the row and col
            if pos in self.positions:  # if the shot would be a hit
                if self.same_ship(self.current_hits[0], pos):  # if the shot will hit the same ship as the first
                    if self.would_sink(row, col):  # if the shot will sink the ship
                        if len(self.hit_backlog) == 0:  # if no hits in backlog, go back to random firing 
                            self.current_hits = []  # reset current_hits
                            self.targets = []  # reset targets
                        else:  # if there are hits in backlog
                            self.current_hits = self.hit_backlog.pop()  # reset current hits to previous ship
                            self.targets = self.next_targets()  # update the targets for the previous ship
                    else:  # the shot hits the same ship but doesn't sink it 
                        self.shot_grid[row][col] = 2  # mark as hit
                        self.current_hits.append((row,col))  # add the hit to current_hits
                        self.targets = self.next_targets()  # update the potential targets
                else:  # if the shot will hit a ship but not the same one as the last shot 
                    if self.would_sink(row, col) == False:  # if the shot will hit a different ship but not sink it
                        self.shot_grid[row][col] = 2  # mark as hit 
                        self.hit_backlog.append(self.current_hits.copy())  # add the current hits to backlog
                        self.current_hits = [(row,col)]  # start firing at new ship 
                        self.targets = self.next_targets()  # get targets for new ship
            else:  # if the shot would not hit a boat
                self.shot_grid[row][col] = 1  # mark the shot as a miss

            return (row, col)  # return the shot coordinates

    def next_targets(self) -> list[tuple[int, int]]:
        targets = []  # list to be returned 
        if len(self.current_hits) == 1:  # Add orthogonally adjacent cells (up, down, left, right)
            row, col = self.current_hits[0]  # retrieve row and col of hit
            for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # iterate through possible directions  
                new_row, new_col = row + d_row, col + d_col  # calculate new position
                if self.valid_shot(new_row, new_col):
                    targets.append((new_row, new_col))  # add potential target
        else:  # if current ship has been hit multiple times 
            # check if horizontally or vertically aligned
            is_horizontal = all(row == self.current_hits[0][0] for row, col in self.current_hits)  
            if is_horizontal:  # if horizontally aligned
                ship_row = self.current_hits[0][0]  # get the row the ship is on
                min_col = min(col for row, col in self.current_hits)  # get the leftmost hit
                max_col = max(col for row, col in self.current_hits)  # get the rightmost hit 
                if self.valid_shot(ship_row, min_col - 1):  # if the new shot to left is valid
                    targets.append((ship_row, min_col - 1))  # add the shot to targets
                if self.valid_shot(ship_row, max_col + 1):  # if the new shot to right is valid
                    targets.append((ship_row, max_col + 1))  # add the shot to targets
            else:  # if vertically aligned
                ship_col = self.current_hits[0][1]  # get the col the ship is on
                min_row = min(row for row, col in self.current_hits)  # get the upper row
                max_row = max(row for row, col in self.current_hits)  # get the lower row
                if self.valid_shot(min_row - 1, ship_col):  # if the shot above is valid
                    targets.append((min_row - 1, ship_col))  # add the shot to targets
                if self.valid_shot(max_row + 1, ship_col):  # if the shot below is valid
                    targets.append((max_row + 1, ship_col))  # add the shot to targets
        return targets  # return the list

    def valid_shot(self, row: int, col: int) -> bool:  # describes if a shot would be valid or not
        if 0 <= row < self.rows and 0 <= col < self.cols:  # check if the position is in bounds
            if self.shot_grid[row][col] == 0:  # check if shot has not been taken yet
                return True  # return True if valid shot
        return False  # return False if invalid

    def would_sink(self, row: int, col: int) -> bool:  # checks if a shot at a given coord would sink the ship
        for ship in self.opponent_grid.ships:  # iterate through opponents ships
            if (row, col) in ship.positions():  # check if the ship exists at given position
                hit_index = ship.positions().index((row,col))  # retrieve the index of the shot 
                for i in range(0,len(ship.hit)):  # iterate through the hits
                    if i != hit_index and ship.hit[i] == 0:  # if any other spot hasn't been hit
                        return False  # return False if the shot would not sink the ship 
                for r, c in ship.positions():  # if shot would sink ship, track by updating shot_grid
                    self.shot_grid[r][c] = 3  # mark the spot as sunk
                return True  # return True if all other spots have been hit
        return False  # return False if ship position not given

    def same_ship(self, prev_shot: tuple[int,int], cur_shot: tuple[int,int]) -> bool: # checks if shots hit same ship
        for ship in self.opponent_grid.ships:  # iterate through the ships in an opponents grid
            positions = ship.positions()  # retrieve the positions of a ship
            if prev_shot in positions and cur_shot in positions:  # if the current shot and previous shot are in positions
                return True  # return True since same ship
        return False  # return False since not same ship

    def hard_shot(self) -> tuple[int, int]:  # returns coordinate that is guaranteed to be a hit
        return self.positions.pop()
