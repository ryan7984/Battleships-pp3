import random 

#function to create the game board 
def create_board(size):
    board = []
    for i in range(size):
        row = ["0"] * size
        board.append(row)
    return board

#function to print the board game 
def print_board(board):
    for row in board:
        print(" ".join(row))

#function to place ships randomly on a row 
def random_row(board):
    return random.randint(0, len(board) - 1)

#function to place ships randomly on a column 
def random_col(board):
    return random.randint(0, len(board[0]) - 1)

#function to run the game
    board = create_board(size)
    print("Ahoy there, let's play Battleships")
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(4):
        print("Turn", turn + 1)
        guess_row = int(input("Guess Row:\n "))
        guess_col = int(input("Guess Col: \n"))

        if guess_row == ship_row and guess_col == ship_col:
            print("Fair play to ye! You sank my Battle Ship.")
            break
        else:
            if guess_row not in range(size) or \
               guess_col not in range(size):
               print("Way off!, thats not even in the sea!")
            
            elif board[guess_row][guess_col] == "X":
                print ("You guessed that one already.")
            else:
                print("Ha ha, you missed my Battleship!")
                board[guess_row][guess_col] = "X"
            print_board(board)
            if turn == 3:
                print("Game Over")

play_battleships(5)
