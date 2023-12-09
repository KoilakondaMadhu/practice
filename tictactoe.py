# Set up the game board as a list
board = ["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-"]

# Define a function to print the game board
def print_board():
    # Display the current state of the game board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Define a function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    # Prompt the player to choose a position from 1-9
    position = input("Choose a position from 1-9: ")

    # Validate the input to ensure it's a number between 1 and 9
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9: ")

    # Convert the input to an integer and adjust for 0-based indexing
    position = int(position) - 1

    # Check if the selected position is already taken
    while board[position] != "-":
        position = int(input("Position already taken. Choose a different position: ")) - 1

    # Update the game board with the player's move
    board[position] = player
    # Display the updated game board
    print_board()

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    if (board[0] == board[1] == board[2] != "-") or \
        (board[3] == board[4] == board[5] != "-") or \
        (board[6] == board[7] == board[8] != "-") or \
        (board[0] == board[3] == board[6] != "-") or \
        (board[1] == board[4] == board[7] != "-") or \
        (board[2] == board[5] == board[8] != "-") or \
        (board[0] == board[4] == board[8] != "-") or \
        (board[2] == board[4] == board[6] != "-"):
        return "win"
    # Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"

# Define the main game loop
def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        # Allow the current player to take their turn
        take_turn(current_player)
        
        # Check if the game is over after the turn
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player for the next turn
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
