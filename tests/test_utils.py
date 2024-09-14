"""
Tests the Grid Class

Authors: Cody Duong, Joon Ooten, Hayden Roy
Date: 2024-09-12
"""

import unittest
from unittest import mock
from src.utils import clear_screen, convert_pos_str_to_row_col

class Test_Utils(unittest.TestCase):
    
    @mock.patch('src.utils.system')  # Mock the system call
    @mock.patch('src.utils.name', 'nt')  # Mock os.name in the src.utils module as 'nt' (Windows)
    def test_clear_screen_windows(self, mock_system):
        # Simulate Windows and verify that 'cls' is called
        clear_screen()
        mock_system.assert_called_with("cls")

    @mock.patch('src.utils.system')  # Mock the system call
    @mock.patch('src.utils.name', 'posix')  # Mock os.name in the src.utils module as 'posix' (Unix)
    def test_clear_screen_unix(self, mock_system):
        # Simulate Unix-based OS and verify that 'clear' is called
        clear_screen()
        mock_system.assert_called_with("clear")

    def test_convert_pos_str_to_row_col_valid(self):
        # Test valid inputs
        self.assertEqual(convert_pos_str_to_row_col("A1"), (0, 0))
        self.assertEqual(convert_pos_str_to_row_col("B2"), (1, 1))
        self.assertEqual(convert_pos_str_to_row_col("C3"), (2, 2))
        self.assertEqual(convert_pos_str_to_row_col("J10"), (9, 9))

    def test_convert_pos_str_to_row_col_invalid(self):
        # Test invalid inputs (expecting ValueError)
        with self.assertRaises(ValueError):
            convert_pos_str_to_row_col("A")  # Missing row

        with self.assertRaises(ValueError):
            convert_pos_str_to_row_col("1A")  # Invalid format

        with self.assertRaises(ValueError):
            convert_pos_str_to_row_col("")  # Empty input

        with self.assertRaises(ValueError):
            convert_pos_str_to_row_col("Z9")  # Out of bounds column

    def test_convert_pos_str_to_row_col_non_string(self):
        # Test non-string input (expecting TypeError)
        with self.assertRaises(TypeError):
            convert_pos_str_to_row_col(123)  # Not a string

        with self.assertRaises(TypeError):
            convert_pos_str_to_row_col(None)  # None type

if __name__ == "__main__":
    unittest.main()
