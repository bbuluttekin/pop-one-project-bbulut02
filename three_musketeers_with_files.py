"""
Allow user to play the game and save it during the game and start saved game at the beginning of the game.
This program keeps track of:
allias for saved game (name of saved game)
time of game saved
users choice, wheather M or R
game board

In order to make saved games presistent this program uses json files to store information in disk about details of all the saved games.

"""
from three_musketeers import *
import json
import os
import datetime


def delete_game(name):
    """
    Function to delete game
    """
    with open("config.json", 'r') as f:
        saved_games = json.load(f)
    for game in saved_games["saved_games"]:
        if game["name"] == name:
            if len(saved_games["saved_games"]) == 1:
                # Remove config.json
                os.remove("config.json")
                print()
                start_with_files()
            else:
                saved_games["saved_games"].remove(game)
                with open("config.json", 'w') as f:
                    json.dump(saved_games, f)
                print("Game deleted!\n")
                print_saved_instructions()


def print_saved_instructions():
    """
    Modified version of print_instructions
    Allows saved game to be picked up by user at the beginning
    """
    print()
    game_choice = input(
        "Would you like to start a new game (N) or continue playing one of the saved games? (S)\n")
    print()
    game_choice = game_choice.upper()
    if game_choice == "N":
        user_side = choose_users_side()
        board = create_board()
        return user_side, board
    elif game_choice == "S":
        # Print list of saved games
        print(
            "Type name of the game to play.\n\nType 'DELETE NAME' to delete a saved game.\n")
        with open("config.json", 'r') as f:
            saved_games = json.load(f)

        print("Name \tDate")
        print("=============================\n")
        for game in saved_games["saved_games"]:
            print(game['name'], "\t", game['date'], "\n")

        user_choice = input(">>> ")
        if user_choice.split(" ")[0].upper() == "DELETE":
            delete_game(user_choice.split(" ")[1])

        # Based on choice load the user_side and board
        for game in saved_games["saved_games"]:
            if game['name'] == user_choice:
                print("Your are playing as {}\n".format(game['user_side']))
                return game['user_side'], game['board']
        print("Cannot find the name!!!\n\n")


def get_users_move_files():
    """
    Modified the get_users_move in a way that it will
    except the SAVE input from user during the game 
    and saves the game
    """
    directions = {'L': 'left', 'R': 'right', 'U': 'up', 'D': 'down'}
    move = input("Your move? ").upper().replace(' ', '')

    # Makes game responsive to save command
    if move == "SAVE":
        game_warning = input("Are you sure you want to save and quit? Y/N\n")

        # Recursive part if player decides not to quit
        if game_warning.upper() == "N":
            return get_users_move_files()

        game_name = input("Please enter a name for the game!\n")

        if os.path.exists("{}/{}".format(os.getcwd(), "config.json")):
            with open("config.json", 'r') as f:
                saved_games = json.load(f)
            all_names = []
            for game in saved_games['saved_games']:
                all_names.append(game['name'])
            if game_name in all_names:
                game_name = input(
                    "Name you entered exist please enter unique name!\n")

        game_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        game_data = {"name": game_name,
                     "date": game_date,
                     "board": get_board(),
                     "user_side": user_side}

        if not os.path.exists("{}/{}".format(os.getcwd(), "config.json")):
            with open("config.json", 'w') as f:
                json.dump({"saved_games": [game_data]}, f)
        else:
            with open("config.json", 'r') as f:
                saved_games = json.load(f)
            saved_games['saved_games'].append(game_data)
            with open("config.json", 'w') as f:
                json.dump(saved_games, f)
            # Add data to json
        exit()

    else:
        # Below this line same of the get_users_move
        if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
                and move[2] in 'LRUD'):
            location = string_to_location(move[0:2])
            direction = directions[move[2]]
            if is_legal_move(location, direction):
                return (location, direction)
        print("Illegal move--'" + move + "'")
        return get_users_move_files()


def move_musketeer_files(user_side):
    """
    Modified version of move_musketeer
    Uses new get_users_move_files function
    """
    if user_side == 'M':
        # Only change to move_musketeer line below
        (location, direction) = get_users_move_files()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(user_side)
    else:  # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)


def move_enemy_files(user_side):
    """
    Modified version of move_musketeer
    Uses new get_users_move_files function
    """
    if user_side == 'R':
        # Only change to move_enemy line below
        (location, direction) = get_users_move_files()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(user_side)
    else:  # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board


def start_with_files():
    """
    Checks if there is a saved games to start playing and if there is no saved game starts the game with new game.
    """
    global user_side
    global board

    # If no saved game start the game as usual
    if not os.path.exists("{}/{}".format(os.getcwd(), "config.json")):
        user_side = choose_users_side()
        board = create_board()
        print_instructions()
        print("Type SAVE at any point of the game to save the game.")
        print_board()
    else:
        user_side, board = print_saved_instructions()
        set_board(board)
        print_board()

    # Same as start function
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
