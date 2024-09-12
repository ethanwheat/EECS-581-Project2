"""
This module contains utility functions useful to all scopes of the Battleship
program

Authors: Kyler Luong, Cody Duong
Date: 2024-09-12
"""

from os import system, name


def clear_screen():
    system("cls" if name == "nt" else "clear")


def convert_pos_str_to_row_col(pos_str: str) -> tuple[int, int]:
    if not (type(pos_str) is str):
        raise TypeError("Expected a pos_str (e.g. A1)")

    if len(pos_str) < 2:
        raise ValueError("Expected a pos_str of at least length 2")

    col, row = pos_str[0], pos_str[1:]

    col_idx = (
        ord(col) - 65
    )  # ord allows the conversion of unicode character into an integer, e.g. A is unicode 65
    row_idx = int(row) - 1  # convert row into integer

    return (row_idx, col_idx)
