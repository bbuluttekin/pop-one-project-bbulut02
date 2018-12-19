"""
Allow user to play the game and save it during the game and start saved game at the beginning of the game.
This program keeps track of:
allias for saved game (name of saved game)
time of game save
users choice, wheather M or R

Logistics
In order to make saved games presistent this program uses json files to store information in disk about details of all the saved games.
"""
from three_musketeers import *
import os


def print_saved_instructions():
    """
    Modified version of print_instructions
    Allows saved game to be picked up by user at the beginning
    """
    print()
    game_choice = input(
        "Would you like to start a new game (N)or continue playing one of the saved games? (S)")
    print()
    game_choice = game_choice.upper()
    if game_choice == "N":
        user_side = choose_users_side()
        return user_side, create_board()
    elif game_choice == "S":
        # Print list of saved games

        # Based on choice load the user_side and board
        pass


def move_musketeer_files(user_side):
    """
    Modified version of move_musketeer
    Responds to SAVE input during the game
    """
    return NotImplementedError


def move_enemy_files(user_side):
    """
    Modified version of move_musketeer
    Responds to SAVE input during the game
    """
    return NotImplementedError


def start_with_files():
    """
    Checks if there is a saved games to start playing and if there is no saved game starts the game with new game.
    """
    if not os.path.exists("{}/{}".format(os.getcwd(), "config.json")):
        user_side = choose_users_side()
        board = create_board()
        print_instructions()
        print("Type SAVE at any point of the game to save the game.")
        print_board()
    else:
        user_side, board = print_saved_instructions()
        print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer_files(user_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy_files(user_side)
            print_board()
        else:
            print("The Musketeers win!")
            break


if __name__ == "__main__":
    start_with_files()
