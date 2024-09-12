'''
Battleship
This program allows its users to be able to play battleships with up to 5 ships
Inputs are the placement of ships and shooting at ships
Outputs are "hit" or "miss"
Authors: Kyler Luong, 
Date: 9/11/24
 '''
import os
#creates the grid to play on
def create_grid(row,col):
    return [['~' for _ in range(row)] for _ in range(col)] # fills grid with ~

#displays the grid
def display_grid(grid, grid_size=10):
    # Create column headers (A-J)
    col = [chr(i) for i in range(65, 65 + grid_size)] #chr allows to bring characters in, A starts at 65 hence and 65 +
    print("  " + " ".join(col))
    
    # Display the grid rows
    for i, row in enumerate(grid):
        print(f"{i+1:<2}" + " ".join(row))
    print()

#The block of code above is meant for creating the grid itself

#this function allows windows users to clear their screen, keeping the board secret
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#gets number of ships
def num_of_ships():
    try:
        num_ships = int(input("How many ships? (1-5): ")) #ask users
        if 1 <= num_ships <= 5: # bounds it needs to fit from user
            return num_ships #returns
        else:
            print("Invalid input of ships") # doesnt fit in bounds
    except ValueError:
        print("Try again (1-5) ships: ") #prints when error aka when there is characters that arent numbers
#this function allows the program to get the number of ships, it asks the user how many ships they want, then if it is within the bounds of 1-5 it will return, if not it will print the input is invalid

#gets the ship sizes based on number of ships user inputted
def get_ship_size(num_ships):
    return [i for i in range(1,num_ships + 1)]
#this function allows the program to get the size of the ship

# Validate the ship's position
def valid_position(grid, pos, ship_size, orientation, grid_size=10): #grid is the grid, position is where the ship is placed, ship_size is how big the size is, orientation is if its vertical or horizontal
    if len(pos) < 2: # users input for the has to be greater than 2, or else it isnt a position they inputed e.g. A1 is len 2 vs 1 is len 1
        return False
    
    col, row = pos[0], pos[1:] #this is a line split for the character of col and number for row
    
    # Convert col to index and row to integer
    col_idx = ord(col.upper()) - 65 #ord allows the conversion of unicode character into an integer, e.g. A is unicode 65
    row_idx = int(row) - 1 #convert row into integer
    
    if not (0 <= col_idx < grid_size and 0 <= row_idx < grid_size): #checks if row and column are within bounds of grid
        return False

    if orientation == 'H': # for orientation that is horizontal
        if col_idx + ship_size > grid_size:  #ship goes beyond edge
            return False
        for i in range(ship_size): # checks to see if any space is taken if so then false
            if grid[row_idx][col_idx + i] != '~':
                return False
    elif orientation == 'V': #for orientations that are vertical
        if row_idx + ship_size > grid_size: # ships goes beyond edge
            return False
        for i in range(ship_size): # checks to see if any space is taken if so then false
            if grid[row_idx + i][col_idx] != '~':
                return False
    return True

# Places ship on grid
def place_ship(grid, ship_size, grid_size=10): 
    while True:
        orientation = input(f"Enter orientation for ship of size {ship_size} (H for horizontal, V for vertical): ").upper() # ask user for what type of orientation
        if orientation in ['H', 'V']: # if H or V
            break
        print("Invalid orientation. Enter 'H' for horizontal or 'V' for vertical.") # if it isnt H or V
    
    while True:
        pos = input(f"Enter the starting position (e.g., A1) for ship of size {ship_size}: ").upper() # ask user for position to place ship
        if valid_position(grid, pos, ship_size, orientation, grid_size): # checks to see if valid
            mark_ship_on_grid(grid, pos, ship_size, orientation) # if valid marks the ship
            break
        print("Invalid position. Try again.") #if not valid

# Mark the ship on the grid
def mark_ship_on_grid(grid, pos, ship_size, orientation):
    col, row = pos[0], pos[1:] # breaks it into line for character columns and number rows
    col_idx = ord(col.upper()) - 65 #converts character into integers
    row_idx = int(row) - 1 #converts into intergers

    if orientation == 'H': # if Horizontal
        for i in range(ship_size): 
            grid[row_idx][col_idx + i] = 'S' # marks ship on position
    elif orientation == 'V': # if vertical
        for i in range(ship_size):
            grid[row_idx + i][col_idx] = 'S' # marks ship on position

# Ship placement for a player
def place_ships(grid):
    num_ships = num_of_ships() #calls to find out number of ship
    ship_sizes = get_ship_size(num_ships) #uses the number of ship to get size
    for ship_size in ship_sizes: #for each ship program 
        display_grid(grid) # shows the board
        place_ship(grid, ship_size) #places ship on board
    print("All ships placed!\n")

# Game setup
def setup_game():
    print("Welcome to Battleship!")
    
    # Player 1
    print("\nPlayer 1, place your ships.")
    player1_grid = create_grid(10,10)
    place_ships(player1_grid)
    clear_screen()
    # Player 2
    print("\nPlayer 2, place your ships.")
    player2_grid = create_grid()
    place_ships(player2_grid)
    clear_screen()
    print("Game setup complete! Ready to start the game.")

if __name__ == "__main__":
    setup_game()
