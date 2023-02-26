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
    player_name = input("What's your name?")
    player_board = create_board(size)
    computer_board = create_board(size)
    print("Ahoy there, let's play Battleships" "Can you sink the computers ships" )
    print("This is your board:")
    print_board(player_board)
    
    computer_ship_row = random_row(board)
    computer_ship_col = random_col(board)

    for turn in range(4):
        print("Turn", turn + 1)
        try:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
        except ValueError:
            print("You can only enter a number")
            continue

        if guess_row == computer_ship_row and guess_col == computer_ship_col:
            print("Fair play to ye! You sank the computers battle Ship.")
            break
        else:
            if guess_row not in range(size) or guess_col not in range(size):
               print("Way off!, thats not even in the sea!")
            elif player_board[guess_row][guess_col] == "X":
               print("You guessed that one already")
            else:
                print("You missed the computers battleship!")
                player_board[guess_row][guess_col] = "X"
            print("Your board:")
            print_board(player_board)
            computer_guess_row = random_row(player_board)
            computer_guess_col = random_col(player_board)
            if computer_guess_row == computer_ship_row and computer_guess_col == computer_ship_col:
                print("Oh no! The computer sank your Battleship!")
                break
            else:
                if computer_guess_row not in range(size) or computer_guess_col not in range(size):
                    print("The computer guessed outside of the board!")
                elif computer_board[computer_guess_row][computer_guess_col] == "X":
                    print("The computer already guessed that one!")
                else:
                    print("The computer missed!")
                    computer_board[computer_guess_row][computer_guess_col] = "X"
            print("The computer's board:")
            print_board(computer_board)
            if turn == 3:
                print("Game Over")


play_battleships(5)



