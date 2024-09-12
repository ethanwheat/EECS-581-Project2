"""
Tests the Grid Class

Authors: Cody Duong, Joon Ooten, Hayden Roy
Date: 2024-09-12
"""

import unittest
from src.utils import *

class Test_Grid(unittest.TestCase):
  def test_clear(self) -> None:
    # TODO mock STDOUT and read that it is empty after running utils.clear_screen
    pass

    # self.assertEqual(stdout.trim(), "")

  def test_convert_pos_str_to_row_col(self) -> None:
    # TODO just test some arbitary in the ranges A1 -> J10, as well as outside

    self.assertEqual(convert_pos_str_to_row_col("A1"), (0, 0))
    #... TODO add more