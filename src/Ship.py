"""
Contains the Ship class

- Keeps track of a ships location and hits

Authors: Cody Duong, Harrison Wendt
Date: 2024-09-12
"""

from typing import Literal, cast
from src.util import *


ShipSize = Literal[1, 2, 3, 4, 5]


class Ship:
    """
    This class is a simple abstraction to store some ship values (and accessing it)
    It has no logic of ships around it or higher game state.
    """

    size: ShipSize  # We only have ship sizes 1-5
    orientation: Literal[None, "H", "V"]
    root: tuple[
        int, int
    ]  # This is the top-left of the ship, a position of -1, -1 indicates an unplaced ship
    hit: list[Literal[0, 1]]  # this indicates where a ship has been hit

    def __init__(self, size: ShipSize) -> None:
        self.size = size
        self.root = (-1, -1)
        self.orientation = None
        self.hit = [0 for _ in range(size)]

    def positions(self) -> list[tuple[int, int]]:
        """The positions the ship occupy starting from the `root` and going in the `orientation`"""
        if self.root == (-1, -1) or self.orientation is None:
            return []  # The ship is not placed on the board yet

        positions: list[tuple[int, int]] = []
        row, col = self.root

        # Horizontal orientation ("H")
        if self.orientation == "H":
            for i in range(self.size):
                positions.append((row, col + i))

        # Vertical orientation ("V")
        elif self.orientation == "V":
            for i in range(self.size):
                positions.append((row + i, col))

        return positions

    def strike(self, pos: tuple[int, int]) -> bool: 
        """This method will attempt to strike the ship at row, index. If it is successful it will reduce the health and return true"""
        #make sure ship is placed
        if self.root == (-1,-1) or self.orientation is None:
            return False
        #get ship positions
        ship_positions = self.positions()

        if pos in ship_positions:
            hit_index = ship_positions.index(pos) #finds index of pos within the ship's position
            if self.hit[hit_index] == 0: #if ship hasn't been hit at that spot, update
                self.hit[hit_index] = 1
                return True
        return False

    def sunk(self) -> bool:
        """Is this ship sunk?"""
        
        #checks if all spaces of a ship have been hit
        return all(hit == 1 for hit in self.hit)
        

    def intersects(self, other: "Ship") -> bool:
        """Check if this ship intersects with another ship."""
        self_positions = set(self.positions())
        other_positions = set(other.positions())

        return not self_positions.isdisjoint(other_positions)

    @staticmethod
    def prompt_orientation() -> Literal["H", "V"]:
        """A helper static method to prompt user input for an orientation"""
        while True:
            orientation = input(
                f"Enter orientation for ship (H for horizontal, V for vertical): "
            ).upper()  # ask user for what type of orientation
            if orientation in ["H", "V"]:  # if H or V
                return cast(Literal["H", "V"], orientation)
            print(
                "Invalid orientation. Enter 'H' for horizontal or 'V' for vertical."
            )  # if it isnt H or V

    @staticmethod
    def prompt_root() -> tuple[int, int]:
        while True:
            pos = input(
                f"Enter the starting position (e.g., A1) for ship of size: "
            ).upper()  # ask user for position to place ship

            try:
                return convert_pos_str_to_row_col(pos)
            except ValueError:
                pass

    def __str__(self) -> str:
        return f"1x{self.size}"
