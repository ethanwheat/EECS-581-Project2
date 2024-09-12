"""
Tests the Grid Class

Authors: Cody Duong, Joon Ooten, Hayden Roy
Date: 2024-09-12
"""

from typing import cast
import unittest
from unittest import mock  # type: ignore
from src.Grid import Grid
from src.Ship import Ship


class Test_Grid(unittest.TestCase):
    grid_input = mock.MagicMock
    ship_input = mock.MagicMock
    clear_screen = mock.MagicMock

    def __init__(self, *argv) -> None:  # type: ignore
        super().__init__(*argv)  # type: ignore
        self._patches = []

    def setUp(self):
        # simulate user input
        self._patches.append(mock.patch("src.Grid.input"))  # type: ignore
        self._patches.append(mock.patch("src.Ship.input"))  # type: ignore

        # suppress output during testing
        self._patches.append(mock.patch("src.Grid.clear_screen", side_effect=lambda *args, **kwargs: None))  # type: ignore
        self._patches.append(mock.patch("src.Grid.print", side_effect=lambda *args, **kwargs: None))  # type: ignore
        self._patches.append(mock.patch("src.Ship.print", side_effect=lambda *args, **kwargs: None))  # type: ignore

        # special named mocks
        self.grid_input = cast(mock.MagicMock, self._patches[0].start())  # type: ignore
        self.ship_input = cast(mock.MagicMock, self._patches[1].start())  # type: ignore
        # remaining unnamed mocks (typically suppressed output)
        self._mocks = [
            cast(mock.MagicMock, [patch.start() for patch in self._patches[2:]])  # type: ignore
        ]

    def tearDown(self):
        # Stop all patches after each test
        for patch in self._patches:  # type: ignore
            patch.stop()  # type: ignore

    def test_1_ship(self) -> None:
        # perform

        # place `1` ship
        # select `1`st ship to place
        # press enter to complete Grid __init__
        self.grid_input.side_effect = ["1", "1", ""]

        # choose 'H' orientation
        # place at 'A1'
        self.ship_input.side_effect = ["H", "A1"]

        mock_ship_1 = Ship(1)
        mock_ship_1.root = (0, 0)
        mock_ship_1.orientation = "H"
        mock_ships = [mock_ship_1]

        grid = Grid(10, 10)

        self.assertEqual(grid.ships, mock_ships)

    def test_2_ship(self) -> None:
        # perform

        # place `2` ships
        # select `2`nd ship to place
        grid_inputs = ["2", "2"]

        # choose 'foo' orientation (invalid)
        # choose 'H' orientation
        # place at 'A1'
        ship_inputs = ["foo", "H", "A1"]

        # select `2`nd ship to place (invalid)
        # select `1`st ship to place
        grid_inputs.extend(["2", "1"])

        # select "V" orientation
        # select "A1" (invalid)
        ship_inputs.extend(["V", "A1"])

        # select `1`st ship to place
        grid_inputs.extend(["1"])

        # select "V" orientation
        # select "B2"
        ship_inputs.extend(["V", "B2"])

        # enter to exit Grid __init__
        grid_inputs.extend([""])

        self.ship_input.side_effect = iter(ship_inputs)
        self.grid_input.side_effect = iter(grid_inputs)

        mock_ship_1 = Ship(1)
        mock_ship_1.root = (1, 1)
        mock_ship_1.orientation = "V"
        mock_ship_2 = Ship(2)
        mock_ship_2.root = (0, 0)
        mock_ship_2.orientation = "H"
        mock_ships = [mock_ship_2, mock_ship_1]

        grid = Grid(10, 10)

        self.assertEqual(grid.ships, mock_ships)

    def test_5_ship(self) -> None:
        # TODO
        pass
