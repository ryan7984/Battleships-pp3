import random 

#function to create the game board 
def create_board(size):
    board = []
    for i in range (size):
        row = ["0"] * size
        board.append(row)
    return board

#function to print the board game 
    for row in board:
        print(" ".join(row))




