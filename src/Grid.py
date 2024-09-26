"""
Contains the Grid class

- Manages state of each players grid
- Keeps track of ships

Authors: Kyler Luong, Cody Duong, Harrison Wendt, Gavin Kirwan
Date: 2024-09-12
Edited: 2024-09-25
"""

import itertools
import random
from typing import Literal
from src.Ship import Ship
from src.utils import *


class Grid:
    """
    This class manages the battleship grid for every player
    """

    ships: list[Ship]
    shot_grid: list[list[Literal[0, 1, 2, 3]]]
    # 0 is no shot made, 1 is shot made (miss), 2 is shot made (hit), 3 is sunk ship
    rows: int
    cols: int

    def __init__(self, rows: int, cols: int, numShips: int, isAI: bool, playingAI: bool) -> None:
        self.rows = rows
        self.cols = cols
        self.shot_grid = [[0 for _ in range(rows)] for _ in range(cols)]
        self.num_ships = numShips
        self.isAI = isAI
        self.playingAI = playingAI

        # Check if is AI
        if (not self.isAI):
            # If not AI then prompt user to place ships
            self.userPlaceShips()
        else:
            # If AI then generate ship placements
            self.aiPlaceShips()

    def aiPlaceShips(self):
        # variant ship sizes
        ships_to_place = [Ship(i) for i in range(1, self.num_ships + 1)]  # type: ignore
        self.ships = []  # type: ignore

        for ship in ships_to_place:
            # Find a valid coordinate and place ship
            while (True):
                letters = [chr(i) for i in range(65, 65+self.cols)]  # Generates ['A', 'B', ..., 'Z']
                numbers = [str(i) for i in range(1, self.rows+1)]
                orientations = ["H", "V"]
                
                # Randomly choose a letter, number, and orientation
                letter = random.choice(letters)
                number = random.choice(numbers)
                orientation = random.choice(orientations)

                # Get combination of letter and number as coordinate
                coordinate = letter + number

                # Set orientation and root
                ship.orientation = orientation
                ship.root = convert_pos_str_to_row_col(coordinate)

                # Check if valid placement, if not retry
                if (not self.place_ship(ship)):
                    break

    # Prompts user to place ships
    def userPlaceShips(self):
        # variant ship sizes
        ships_to_place = [Ship(i) for i in range(1, self.num_ships + 1)]  # type: ignore
        self.ships = []  # type: ignore

        # prompt ship placement
        while len(ships_to_place) > 0:
            self.display_ships()
            print("\nShips to place:")
            for i, value in enumerate(ships_to_place):
                print(f"{i+1}: {value}")
            try:
                ship_index = int(input("Select a ship (by index) to place: "))
                if 1 <= ship_index < len(ships_to_place) + 1:
                    ship = ships_to_place.pop(ship_index - 1)
                    ship.orientation = Ship.prompt_orientation()
                    ship.root = Ship.prompt_root()
                    invalid_ship = self.place_ship(ship)
                    if invalid_ship:
                        print("Invalid ship placement, please try again.")
                        ships_to_place.insert(ship_index, invalid_ship)
                else:
                    print("Invalid ship index, please try again.")
            except ValueError:
                print("Invalid ship index, please try again.")
                continue

        print("\nYour ships!")
        self.display_ships()

        if (not self.playingAI):
            input("Enter to continue to next player setup")
        else:
            input("Enter to continue")

        clear_screen()

    def strike(self, pos: tuple[int, int]) -> None:
        #
        # check self.ships, and try ship.strike() on every ship, if true then we hit a ship (end early end loop), if false for all then no ships were hit
        # if ship.strike() is successful, check if we sunk the ship with ship.sunk(), print appropriate messages for hitting, missing, or sinking
        # update the shot_grid to reflect whether we missed at pos, hit at pos, and then if a ship sunk update all parts of the grid where sunk

        """Handles the strike on the grid at given position"""
        row, col = pos
        hit_any_ship = False

        # Go through each ship and check if position hits any of them
        for ship in self.ships:  # go through all ships
            if ship.strike(pos):  # if ship is hit
                hit_any_ship = True  # set flag to true
                print(f"{'Player 2 ' if self.playingAI and not self.isAI else ''}Hit at {pos}!")

                if ship.sunk():
                    print(f"{'Player 2 ' if self.playingAI and not self.isAI else 'You '}sunk a {ship}!")
                    # update grid with sunk ships
                    for ship_pos in ship.positions():
                        sr, sc = (
                            ship_pos  # seperates position coordinates into two variables (ship row, and ship column)
                        )
                        self.shot_grid[sr][sc] = 3  # mark sunk parts on shot grid
                else:
                    self.shot_grid[row][
                        col
                    ] = 2  # if ship not sunk but hit update shot grid to 2
                break
        if not hit_any_ship:
            print(f"{'Player 2 ' if self.playingAI and not self.isAI else ''}Miss at {pos}.")
            self.shot_grid[row][col] = 1

        if (self.isAI):
            self.display_shots()

    def place_ship(self, ship: Ship) -> None | Ship:
        """Places a valid ship into the grid, if invalid it will instead return the ship"""

        if self.validate_ship(ship):
            self.ships.append(ship)
        else:
            return ship

    def __print_headers(self) -> None:
        """Create column headers (A-J)"""
        col = [
            chr(i) for i in range(65, 65 + self.cols)
        ]  # chr allows to bring characters in, A starts at 65 hence and 65 +
        print("  " + " ".join(col))

    def __format_grid(self) -> list[list[str]]:
        """Formats a shot_grid into a meaningful grid of strings using __format_cell"""
        return [[Grid.__format_cell(cell) for cell in row] for row in self.shot_grid]

    @staticmethod
    def __format_cell(state: Literal[0, 1, 2, 3]) -> str:
        if state == 0:
            return "~"  # No shot
        elif state == 1:
            return "X"  # Miss
        elif state == 2:
            return "H"  # Hit
        elif state == 3:
            return "H"  # Sunk? Should there really be a seperate indicator

        if not (type(state) is int):
            raise TypeError("Expected state to be int")

        raise ValueError("State out of bounds")

    def display_ships(self) -> None:
        self.__print_headers()

        ship_grid = self.__format_grid()
        for pos in itertools.chain.from_iterable(
            [ship.positions() for ship in self.ships]
        ):
            row, col = pos
            if ship_grid[row][col] == "~":
                ship_grid[row][
                    col
                ] = "S"  # if we haven't been struck then indicate it as a ship

        # Display the grid rows
        for i, row in enumerate(ship_grid):
            print(f"{i+1:<2}" + " ".join(row))
        print()

    def display_shots(self) -> None:
        self.__print_headers()

        # Display the grid rows
        for i, row in enumerate(self.__format_grid()):
            print(f"{i+1:<2}" + " ".join(row))
        print()

    def validate_ship(self, ship: Ship) -> bool:
        """Checks if this ship is valid for the current Grid"""
        orientation = ship.orientation
        row_idx, col_idx = ship.root
        ship_size = ship.size

        if orientation == "H":  # for orientation that is horizontal
            if col_idx + ship_size > self.rows:  # ship goes beyond edge
                return False

        elif orientation == "V":  # for orientations that are vertical
            if row_idx + ship_size > self.cols:  # ships goes beyond edge
                return False

        # if we have overlapping ships
        if any([other_ship.intersects(ship) for other_ship in self.ships]):
            return False

        return True
