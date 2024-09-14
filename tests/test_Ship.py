"""
Tests the Ship Class

Authors: Joon Ooten, Hayden Roy
Date: 2024-09-12
"""

import unittest
from src.Ship import Ship

class Test_Ship(unittest.TestCase):
    def test_ship_initialization(self):
        # Test that a ship is initialized with the correct size, unplaced, and no hits
        ship = Ship(3)
        
        # Check the ship's size
        self.assertEqual(ship.size, 3)
        
        # Check that the ship's root position is unplaced (-1, -1)
        self.assertEqual(ship.root, (-1, -1))
        
        # Check that the orientation is None (not placed yet)
        self.assertIsNone(ship.orientation)
        
        # Check that the ship has no hits yet
        self.assertEqual(ship.hit, [0, 0, 0])

    def test_ship_placement(self):
        # Test setting the ship's root position and orientation
        ship = Ship(3)
        ship.root = (2, 2)
        ship.orientation = "H"

        # Check the ship's root position
        self.assertEqual(ship.root, (2, 2))
        
        # Check the ship's orientation
        self.assertEqual(ship.orientation, "H")

        # Check the ship's positions (from root in horizontal orientation)
        self.assertEqual(ship.positions(), [(2, 2), (2, 3), (2, 4)])

    def test_ship_strike(self):
        # Test the strike() method to ensure hits are registered correctly
        ship = Ship(3)
        ship.root = (1, 1)
        ship.orientation = "V"
        
        # Strike the ship at a valid position
        result = ship.strike((1, 1))  # Hit the first part of the ship
        self.assertTrue(result)
        self.assertEqual(ship.hit, [1, 0, 0])  # First part should be hit

        # Strike the second part of the ship
        result = ship.strike((2, 1))  # Hit the second part
        self.assertTrue(result)
        self.assertEqual(ship.hit, [1, 1, 0])  # Second part should be hit

        # Strike at an invalid position (miss)
        result = ship.strike((4, 4))  # Should be a miss
        self.assertFalse(result)
        self.assertEqual(ship.hit, [1, 1, 0])  # No change to hit array

    def test_ship_sunk(self):
        # Test the sunk() method to check if a ship is sunk correctly
        ship = Ship(2)
        ship.root = (0, 0)
        ship.orientation = "H"
        
        # Initially the ship should not be sunk
        self.assertFalse(ship.sunk())

        # Strike both parts of the ship to sink it
        ship.strike((0, 0))
        ship.strike((0, 1))

        # Now the ship should be sunk
        self.assertTrue(ship.sunk())

if __name__ == "__main__":
    unittest.main()
