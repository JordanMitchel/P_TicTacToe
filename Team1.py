# Tic Tac Toe

import random

# The board to start with
the_board = [" "] * 10


# This function displays the board
def print_board(board):
    print(board[1], "|", board[2], "|", board[3])
    print("--+---+--")
    print(board[4], "|", board[5], "|", board[6])
    print("--+---+--")
    print(board[7], "|", board[8], "|", board[9])
    print(' \n  ')


# Function to set markers for players
def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1 chose X or O: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Function to place palyer's marker on board
def place_marker(board, player_marker, position):
    board[position] = player_marker


def win_check(board, marker):
    return (board[1] == board[2] == board[3] == marker or
            board[4] == board[5] == board[6] == marker or
            board[7] == board[8] == board[9] == marker or
            board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or
            board[3] == board[6] == board[9] == marker or
            board[1] == board[5] == board[9] == marker or
            board[3] == board[5] == board[7] == marker)


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose position: (1-9) '))

    return position


def replay():
    choice = input('Play again? Enter Y or N: ').upper()

    return choice == 'Y'


# This is where the game starts

ready_to_play = input('Ready to play? Y or N? ').upper()

if ready_to_play == 'Y':
    game = True
else:
    game = False


# The game is held in this while loop
while game:
    the_board = [" "] * 10
    player1_marker, player2_marker = player_input()

    # The for loop represents the number of goes the players will have in total
    for i in range(9):
        # If i is even it will be player ones turn
        if i % 2 == 0:
            print_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            print_board(the_board)

            if win_check(the_board, player1_marker):
                print("Player 1 has won!")
                break

        # If i is odd it will be player twos turn
        else:
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            print_board(the_board)
            if win_check(the_board, player2_marker):
                print("Player 2 has won!")
                break

    # This calls for a function to check if the board is full, if so will print tie
    done = full_board_check(the_board)
    if done:
        print("It's a tie!")

        # Break out of while loop on replay()
    if replay():
        game = True
    else:
        break