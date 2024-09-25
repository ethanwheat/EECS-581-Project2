"""
Contains the Battleship class

- Handles player setup and controls
- Ends game upon certain conditions

Authors: Kyler Luong, Cody Duong, Harrison Wendt
Date: 2024-09-12
"""

from typing import Literal
from src.Grid import Grid
from src.utils import *


class Battleship:
    player0: Grid
    player1: Grid
    turn: Literal[0, 1]
    isAI: bool

    def __init__(self, rows: int = 10, cols: int = 10) -> None:
        """
        The setup function for the Battleship game

        Each player has a Grid, and each Grid has Ships

        Args:
          rows (str, optional): The number of rows in this Battleship game. Defaults to `10`
          cols (int, optional): The number of columns in this Battleship game. Defaults to `10`
        """
        self.isAI, self.difficulty = self.gameOption()
        numShips = self.__prompt_number_of_ships()
        self.player1 = Grid(rows, cols, numShips, False, self.isAI)
        self.player2 = Grid(rows, cols, numShips, self.isAI, self.isAI)
        self.turn = 0  # start with p1 turn, 0 for p1 and 1 for p2)

    # Ask whether player wants to play against another player or ai
    def gameOption(self):
        print("Choose an option:")
        print("1.) Two Players")
        print("2.) Against AI")

        mode = input()

        # Check if valid option
        if (mode not in ["1","2"]):
            print("Invalid Option\n")
            return self.gameOption()

        # Two players was picked
        if (mode == "1"):
            return False, None

        # AI was picked
        return True, self.aiDifficulty()

    def aiDifficulty(self):
        # Prompt for difficulty
        print("Choose difficulty:")
        print("1.) Easy")
        print("2.) Medium")
        print("3.) Hard")

        difficulty = input()

        # Check if valid option
        if (difficulty not in ["1","2","3"]):
            print("Invalid Option\n")
            return self.aiDifficulty()

        # Return difficulty
        return difficulty

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

    def play(self) -> None:
        # raise Exception("Not implemented yet")

        # TODO
        # Check the self.turn for which player turn

        # display both our grid and the enemy grid.
        # OUR.display_ships (where we can view our own ship positions and health as well as enemy shots)
        # maybe print OUR ships remaining?
        # ENEMY.display_shots (where we have attempted shots)
        # maybe print ENEMY ships remaining?

        # prompt the user for a position to strike at
        # a useful function might be `convert_pos_str_to_row_col`
        # check is on board and that we haven't already hit this position, if we have then prompt for a different position

        # strike at the grid of the ENEMY player with Grid.strike

        # end turn

        while True:
            # Determine the current player and the enemy
            current_player = self.player1 if self.turn == 0 else self.player2
            enemy_player = self.player2 if self.turn == 0 else self.player1

            # If is player
            if((not self.isAI) or self.turn == 0):
                # Display both current and enemy grids
                print(f"\nPlayer {self.turn + 1}'s Turn\n")
                print("Your Grid:")
                current_player.display_ships()  # Show our ships and enemy shots
                print("\nEnemy Grid:")
                enemy_player.display_shots()  # Show our shots on the enemy

                # Get a valid strike position from the player
                while True:
                    try:
                        pos = input("Enter the position to strike (e.g., A1): ").upper()
                        strike_pos = convert_pos_str_to_row_col(pos)

                        # Check if the position is on the board and hasn't been struck already
                        row, col = strike_pos
                        if (
                            0 <= row < current_player.rows
                            and 0 <= col < current_player.cols
                            and enemy_player.shot_grid[row][col] == 0
                        ):
                            break
                        else:
                            print("Invalid position or position already struck. Try again.")
                    except ValueError:
                        print("Invalid input. Use format like 'A1'. Try again.")

                # Strike the enemy player's grid
                enemy_player.strike(strike_pos)
            else:                
                # Shoot shots according to difficulty
                if (self.difficulty == "1"):
                    print("Easy shot")
                    # Call easy mode function on AI and pass
                    # that as argument in strike
                    # enemy_player.strike(strike_pos)
                elif (self.difficulty == "2"):
                    print("Medium shot")
                    # Call medium mode function on AI and pass
                    # that as argument in strike
                    # enemy_player.strike(strike_pos)
                elif (self.difficulty == "3"):
                    print("Hard shot")
                    # Call hard mode function on AI and pass
                    # that as argument in strike
                    # enemy_player.strike(strike_pos)

            # Check if the game should end (all ships sunk)
            if all(ship.sunk() for ship in enemy_player.ships):
                print(f"Player {self.turn + 1} wins!")
                break

            # End turn and switch to the other player
            if (not self.isAI):
                input("Press Enter to end your turn and pass to the next player...")
                clear_screen()
            elif (self.turn == 0):
                input("Press Enter to continue...")
                clear_screen()

            # Toggle between 0 and 1
            self.turn = 1 - self.turn  # type: ignore

        input("Press Enter to quit game.")
        clear_screen()
