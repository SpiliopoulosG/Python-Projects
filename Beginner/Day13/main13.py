
# TicTacToe

def clear_output():
    print('\n' * 100)


def makes_board():
    return ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(board):
    print('| ' + board[7] + '|', board[8] + '|', board[9] + '|')
    print('---------')
    print('| ' + board[4] + '|', board[5] + '|', board[6] + '|')
    print('---------')
    print('| ' + board[1] + '|', board[2] + '|', board[3] + '|')


# Asks the user whether they want to play 'X' or 'O'
def player_input():
    while True:
        first_player_marker = input("Would you like to play as 'X' or as 'O' ?")
        if first_player_marker.upper() == 'X':
            return first_player_marker.upper(), "O"
        if first_player_marker.upper() == 'O':
            return first_player_marker.upper(), "X"


# Places Marker
def place_marker(board, marker, play):
    board[play] = marker
    return board[play]


# Checks if someone has won
def win_check(board):
    if board[1] == board[2] == board[3] != " ":
        print(f'The player with the {board[1]} has won')
        return True
    if board[4] == board[5] == board[6] != " ":
        print(f'The player with the {board[4]} has won')
        return True
    if board[7] == board[8] == board[9] != " ":
        print(f'The player with the {board[7]} has won')
        return True
    if board[1] == board[4] == board[7] != " ":
        print(f'The player with the {board[1]} has won')
        return True
    if board[2] == board[5] == board[8] != " ":
        print(f'The player with the {board[2]} has won')
        return True
    if board[3] == board[6] == board[9] != " ":
        print(f'The player with the {board[3]} has won')
        return True
    if board[1] == board[5] == board[9] != " ":
        print(f'The player with the {board[1]} has won')
        return True
    if board[3] == board[5] == board[7] != " ":
        print(f'The player with the {board[3]} has won')
        return True
    return False


# Check if the space chosen is available
def space_check(board, play):
    if board[play] == ' ':
        return True
    else:
        return False


# Checks whether all board is full
def full_board_check(board):
    for i in range(len(board)):
        if board[i] == ' ':
            return False
        else:
            continue
    print("The board is full!")
    return True


# Player Choice on board
def player_choice(board):
    while True:
        int_type = False
        between_1_9 = False
        while int_type is False or between_1_9 is False:
            move = input('Which position to place the mark?')
            if move.isdigit() is True:
                choice = int(move)
                int_type = True
            else:
                print('Not an Integer')
            if choice in range(1, 10):
                between_1_9 = True
            else:
                print('Not withing range')
        if space_check(board, choice):
            return choice
        else:
            print('Position already taken,Try again')


# Replay
def replay():
    while True:
        play_again = input("Do you want to play again? Enter 'yes' or 'no'.")
        if play_again.lower() == 'yes':
            return True
        elif play_again.lower() == 'no':
            return False
        else:
            print('Invalid Input try again')


# Game
while True:
    # Set the game up here
    print('Welcome to Tic Tac Toe!')
    board = makes_board()
    display_board(board)
    player1_marker, player2_marker = player_input()
    # Starts The Game Loop
    while True:
        clear_output()
        display_board(board)
        # Player 1 Turn
        play = int(player_choice(board))
        place_marker(board, player1_marker, play)
        if win_check(board) is True or full_board_check(board) is True:
            display_board(board)
            break
        clear_output()
        # Player2's turn.
        display_board(board)
        play = int(player_choice(board))
        place_marker(board, player2_marker, play)
        clear_output()

        if win_check(board) is True or full_board_check(board) is True:
            display_board(board)
            break
    if not replay():
        break
