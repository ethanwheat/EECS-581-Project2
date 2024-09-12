"""
Contains the Grid class

- Manages state of each players grid
- Keeps track of ships

Authors: Cody Duong
Date: 2024-09-12
"""

import itertools
from typing import Literal
from src.Ship import Ship
from src.util import *


class Grid:
    """
    This class manages the battleship grid for every player
    """

    ships: list[Ship]
    shot_grid: list[list[Literal[0, 1, 2, 3]]]
    # 0 is no shot made, 1 is shot made (miss), 2 is shot made (hit), 3 is sunk ship
    rows: int
    cols: int

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.shot_grid = [[0 for _ in range(rows)] for _ in range(cols)]

        num_ships = Grid.__prompt_number_of_ships()

        # variant ship sizes
        ships_to_place = [Ship(i) for i in range(1, num_ships + 1)]  # type: ignore
        self.ships = []  # type: ignore

        # prompt ship placement
        while len(ships_to_place) > 0:
            self.display_ships()
            print("\nShips to place:")
            for i, value in enumerate(ships_to_place):
                print(f"{i}: {value}")
            try:
                ship_index = int(input("Select a ship (by index) to place: "))
                if 0 <= ship_index < len(ships_to_place):
                    ship = ships_to_place.pop(ship_index)
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
        input("Enter to continue to next player setup")

        clear_screen()

    def strike(self, pos: tuple[int, int]) -> None:
        # TODO
        # check self.ships, and try ship.strike() on every ship, if true then we hit a ship (end early end loop), if false for all then no ships were hit
        # if ship.strike() is successful, check if we sunk the ship with ship.sunk(), print appropriate messages for hitting, missing, or sinking
        # update the shot_grid to reflect whether we missed at pos, hit at pos, and then if a ship sunk update all parts of the grid where sunk
        pass

    @staticmethod
    def __prompt_number_of_ships() -> int:
        """Prompts the user for a number of ships they want to place"""
        while True:
            try:
                num_ships = int(input("How many ships? (1-5): "))  # ask users
                if 1 <= num_ships <= 5:  # bounds it needs to fit from user
                    return num_ships
                else:
                    print(
                        "Invalid number of ships, expected between 1-5 ships"
                    )  # doesnt fit in bounds
            except ValueError:
                print("Invalid value for ships")

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
