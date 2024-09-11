'''
Battleship
This program allows its users to be able to play battleships with up to 5 ships
Inputs are the placement of ships and shooting at ships
Outputs are "hit" or "miss"
Authors: Kyler Luong, 
Date: 9/11/24
 '''

def create_grid(row, col):
    grid = [[0 for _ in range(col)] for _ in range(row)]
    return grid
grid = create_grid(10,10)
for row in grid:
    print(row)