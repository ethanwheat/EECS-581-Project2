'''
Battleship
This program allows its users to be able to play battleships with up to 5 ships
Inputs are the placement of ships and shooting at ships
Outputs are "hit" or "miss"
Authors: Kyler Luong, 
Date: 9/11/24
 '''

def create_grid(row,col):
    # Create the grid with row numbers and column letters
    grid = []

    # Generate header for columns (letters A-J), characters start at 65 and on
    header = [' '] + [chr(65 + i) for i in range(col)]
    grid.append(header)

    # Generate rows with row numbers (1-10) 
    for i in range(row):
        row = [i + 1] + ["-" for _ in range(col)]
        grid.append(row)

    return grid

#The block of code above is meant for creating the grid itself
# BELOW NEEDS WORKED ON
def ship_size(num_of_ships):
    if num_of_ships == 1: # if only 1 ship
        ship_placement = input("where do you want the ship? (e.g., A5)").upper()
        coordinates(ship_placement)
        return
    
    elif num_of_ships == 2: #if 2 ships
        i = 0
        while i < num_of_ships:
            ship_placement = input("where do you want ship 1? (e.g., A5)").upper()
            coordinates(ship_placement)
        ship_placement = input("where do you want ship 2? (This is a 1x2 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        return
    
    elif num_of_ships == 3:
        ship_placement = input("where do you want ship 1? (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 2? (This is a 1x2 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 3? (This is a 1x3 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        return
    
    elif num_of_ships == 4:
        ship_placement = input("where do you want ship 1? (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 2? (This is a 1x2 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 3? (This is a 1x3 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 4? (This is a 1x4 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        return
    
    elif num_of_ships == 5:
        ship_placement = input("where do you want ship 1?  (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 2? (This is a 1x2 ship)  (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 3? (This is a 1x3 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 4? (This is a 1x4 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        ship_placement = input("where do you want ship 5? (This is a 1x5 ship) (e.g., A5)").upper()
        coordinates(ship_placement)
        return
    
    else:
        print("Invalid number of ships")
        again = input("Try again: (1-5)")
        ship_size(again)

#this block of code allows users to input where they want their ship and if they dont have the right number of ships it will ask them to try again
def coordinates(ship_placement):
    while True:
        try:
            pos = ship_placement
            if len(pos) < 2:
                raise ValueError("Invalid input")
            col = ord(pos[0]) - 65
            row = int(pos[1:]) - 1
            if 0 <= row < 10 and 0 <= col < 10:
                return row,col
        except ValueError:
            print("Invalid input, try again")
#ABOVE NEEDS WORKED ON
#Asks the user for the number of ships they want
num_of_ships = input("How many ships do you want? (1-5) :")
#Calls the function ship_size in order to determine how many ships and size of ships
ship_size(num_of_ships)
#Creates the grid
grid = create_grid(10,10)

#Prints the grid
for row in grid:
    print(row)
