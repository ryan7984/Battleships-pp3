import random 

#Function to create the game board 
def create_board(size):
    board = []
    for i in range(size):
        row = ["0"] * size
        board.append(row)
    return board

#Function to print the board to the game 
def print_board(board):
    for row in board:
        print(" ".join(row))

#Function to pick a ship on the board on a row
def random_row(board):
    return random.randint(0, len(board) - 1)

#Function to pick a ship on the board on a coloumn
def random_col(board):
    return random.randint(0, len(board[0]) - 1)

#Main function to run the game 
def play_battleships(size):
    board = create_board(size)
    print("Ahoy there, let's play Battleships")
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(4):
        print("Turn", turn + 1)
        try:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
        except ValueError:
            print("You can only enter a number")
            continue

        if guess_row == ship_row and guess_col == ship_col:
            print("Fair play to ye! You sank my Battle Ship.")
            break
        else:
            if guess_row not in range(size) or \
               guess_col not in range(size):
               print("Way off!, thats not even in the sea!")
            elif board[guess_row][guess_col] == "X":
               print("You guessed that one already")
            else:
                print("You missed my Battleship! You need to go to specsavers")
                board[guess_row][guess_col] = "X"
            print_board(board)
            if turn == 3:
                print("Game Over")


play_battleships(5)



