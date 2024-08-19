import time
import os
import random
from typing import Optional

# Define game loading function (pretending to load)
def load_game() -> None:
    # Initial message
    print("Tic Tac Toe game initiated")
    time.sleep(1)
    os.system("clear")
    
    # Loading game message
    for i in range(4):
        print(f"Game is loading{'.' * i}")
        time.sleep(1)
        os.system("clear")
    
    # Game loaded successfully message
    print("Game is loaded successfully!")
    time.sleep(1)
    os.system("clear")

# Choose a symbol player would like to play as
def choose_symbol() -> str:
    while True:
        symbol = input("Choose your symbol (O or X): ")
        if symbol in ("X", "x", "O", "o"):
            return symbol.upper()
        print("Invalid choice. Please select O or X.")

# Define Board class that will be used for the game
class Board:
    # Define amount of cells used in the board and win conditions
    def __init__(self) -> None:
        # Create cells
        self.cells  = [" "] * 10
        # Define winning conditions
        self.win_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    
    # Define function that will display the board and assign the cells to the board  
    def display(self) -> None:
        # Generate 3 cells on the top row
        print("\n")
        print("\t     |     |     ")
        print("\t  %s  |  %s  |  %s  " %(self.cells[1], self.cells[2], self.cells[3]))
        print("\t_____|_____|_____")
        
        # Generate 3 cells on the middle row
        print("\t     |     |     ")
        print("\t  %s  |  %s  |  %s  " %(self.cells[4], self.cells[5], self.cells[6]))
        print("\t_____|_____|_____")
        
        # Generate 3 cells on the bottom row
        print("\t     |     |     ")
        print("\t  %s  |  %s  |  %s  " %(self.cells[7], self.cells[8], self.cells[9]))
        print("\t     |     |     ")
        print("\n")
    
    # Define a fuction for user to choose a cell to play and validate user input
    def get_user_cell_no(self) -> int:
        # Start endless loop
        while True:
            # Gather user input
            user_cell = input("Insert a cell number (1 - 9): ")
            # Validate if number is an actual number
            if not user_cell.isdigit():
                print("The value is not a number, please try again.")
                continue
            user_cell = int(user_cell)
            # Validate if an actuall number is between 1 and 9
            if user_cell < 1 or user_cell > 9:
                print("The number must be between 1 and 9. Please try again.")
                continue
            return user_cell
    
    # Define a fuction to validate if cell is empty and update the cells
    def update_cell(self, cell_no: int, player: str) -> None:
        # Start endless loop
        while True:
            # If the cell is empty, update the cell with user symbol
            if self.cells[cell_no] == " ":
                self.cells[cell_no] = player
                break
            # If the cell is already taken, request user to choose a cell again
            else:
                print("Cell is taken. Please choose another cell.")
                # Request user input with validation from function get_user_cell_no
                cell_no = self.get_user_cell_no() 
    
    # Define a function to check if the game has been won yet
    def check_win(self) -> Optional[str]:
        # Iterate over a list of winning contitions
        for w in self.win_conditions:
            # Check if winning conditions has been met yet.
            if self.cells[w[0]] == self.cells[w[1]] == self.cells[w[2]] == "X":
                return "X"
            elif self.cells[w[0]] == self.cells[w[1]] == self.cells[w[2]] == "O":
                return "O"
        return None # No winner yet
    
    # Define a function to check if the board is full and if the game is already a tie.
    def is_full(self) -> bool:
        return " " not in self.cells[1:] # Check if the board is full excluding the 0th index by checking if there's any " " (spaces) left in the cells 1-9

# Define a function to clean and refresh the screen
def refresh_screen(board: Board) -> None:
    # Clear the screen
    os.system("clear")
    
    # Display the board
    board.display()

# Define a function for AI to make a move
def ai_move(board: Board, player: str) -> None:
    # Define available moves for AI to use
    available_moves = [i for i, x in enumerate(board.cells) if x == " " and i != 0] # Iterates over cells in class object to find empty cells
    # Randomize a choice from available cells
    move = random.choice(available_moves)
    # Update the board with AI move.
    board.update_cell(move, player)
        
# Main game loop
def play_game() -> None:
    while True:
        load_game()
        board = Board()
        
        # Define a player symbol with the use of choose_symbol function
        player1_symbol = choose_symbol()
        player2_symbol = "O" if player1_symbol == "X" else "X"
        os.system("clear")
        
        # Print what symbol 
        print(f"Player will be playing {player1_symbol}")
        print(f"AI will be playing as {player2_symbol}")
        time.sleep(2)
        
        # Define current_player variable so that the player is always first to start
        current_player = player1_symbol
        
        # Start an endless loop
        while True:
            # Refresh the screen to keep it clean
            refresh_screen(board)
            
            # Gather inputs required for the player to make a move
            if current_player == player1_symbol:
                # Gather user input on what cell they'd like to make a move at
                cell_no = board.get_user_cell_no()
                # Update the board with new player move
                board.update_cell(cell_no, current_player)
            else:
                # Request AI move if its AI's turn.
                ai_move(board, player2_symbol)
            
            # Define a winner variable while calling check_win validation
            winner = board.check_win()
            
            # If there's a winner run this part of the code
            if winner:
                refresh_screen(board)
                print(f"Player {winner} has won the game!")
                break
            
            # If there's no winner and there's no more empty cells left, run this code.
            elif board.is_full():
                refresh_screen(board)
                print("The game is a draw")
                break
            current_player = "O" if current_player == "X" else "X"
        
        restart = input("Would you like to restart the game and play again? (Y/N) ")
        if restart != "Y":
            print("Thank you for playing the game!")
            break
        

play_game()