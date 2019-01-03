# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.


def create_board():
    global board
    """
    Creates the initial Three Musketeers board and makes it globally available (That is, it doesn't have to be passed around as a parameter.) 'M' represents a Musketeer, 'R' represents one ofCardinal Richleau's men, and '-' denotes an empty space.
    """
    m = 'M'
    r = 'R'
    board = [[r, r, r, r, m],
             [r, r, r, r, r],
             [r, r, m, r, r],
             [r, r, r, r, r],
             [m, r, r, r, r]]
    return board


def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board


def get_board():
    """
    Just returns the board. Possibly useful for unit tests.
    """
    return board


def string_to_location(s):
    """
    Given a two-character string (such as 'A5'), returns the designated location as a 2-tuple (such as (0, 4)). The function should raise ValueError exception if the input is outside of the correct range (between 'A' and 'E' for s[0] and between '1' and '5' for s[1]
    """
    if s[0].upper() not in ['A', 'B', 'C', 'D', 'E']:
        raise ValueError(
            "Wrong position given column should be between A to E!")
    if int(s[1]) > 5:
        raise ValueError("Wrong value!")
    for index, letter in enumerate(['A', 'B', 'C', 'D', 'E']):
        if s[0] == letter:
            first_pos = index
    second_pos = int(s[1]) - 1
    return (first_pos, second_pos)  # Replace with code


def location_to_string(location):
    """
    Returns the string representation of a location.
    Similarly to the previous function, this function should
    raises ValueError exception if the input is outside of the
    correct range
    """
    if location[0] not in range(5) or location[1] not in range(5):
        raise ValueError("Wrong range given!")
    for index, letter in enumerate(['A', 'B', 'C', 'D', 'E']):
        if index == location[0]:
            first_pos = letter
    second_pos = location[1] + 1
    return '{}{}'.format(first_pos, second_pos)  # Replace with code


def at(location):
    """
    Returns the contents of the board at the given location.
    You can assume that input will always be in correct range.
    """
    return board[location[0]][location[1]]


def all_locations():
    """Returns a list of all 25 locations on the board."""
    all_loc = []
    for i in range(5):
        for j in range(5):
            all_loc.append((i, j))
    return all_loc  # Replace with code


def adjacent_location(location, direction):
    """
    Return the location next to the given one, in the given direction. Does not check if the location returned is legal on a 5x5 board. You can assume that input will always be in correct range.
    """
    direction = direction.lower()
    (row, column) = location
    new_location = None
    if direction == 'right':
        new_location = (row, column + 1)
    elif direction == "left":
        new_location = (row, column - 1)
    elif direction == "down":
        new_location = (row + 1, column)
    elif direction == "up":
        new_location = (row - 1, column)
    return new_location  # Replace with code


def is_legal_move_by_musketeer(location, direction):
    """
    Tests if the Musketeer at the location can move in the direction. You can assume that input will always be in correct range. Raises ValueError exception if at(location) is not 'M'
    """
    is_musketeer_legal = False
    if at(location) != 'M':
        raise ValueError("No Musketeer in the given location!")
    new_loc = adjacent_location(location, direction)
    if new_loc[0] in range(5) and new_loc[1] in range(5):
        is_musketeer_legal = at(new_loc) == "R"
    # Replace with code
    return is_musketeer_legal


def is_legal_move_by_enemy(location, direction):
    """
    Tests if the enemy at the location can move in the direction. You can assume that input will always be in correct range. Raises ValueError exception if at(location) is not 'R'
    """
    is_enemy_legal = False
    if at(location) != "R":
        raise ValueError("No Cardinals men in that location!")
    new_loc = adjacent_location(location, direction)
    if new_loc[0] in range(5) and new_loc[1] in range(5):
        is_enemy_legal = at(new_loc) == "-"
    # Replace with code
    return is_enemy_legal


def is_legal_move(location, direction):
    """
    Tests whether it is legal to move the piece at the location
    in the given direction. You can assume that input will always be in correct range.
    """
    is_legal = False
    if at(location) == "M":
        is_legal = is_legal_move_by_musketeer(location, direction)
    elif at(location) == "R":
        is_legal = is_legal_move_by_enemy(location, direction)
    return is_legal  # Replace with code


def can_move_piece_at(location):
    """
    Tests whether the player at the location has at least one move available. You can assume that input will always be in correct range. You can assume that input will always be in correct range.
    """
    can_move = False
    for direction in ["up", "down", "left", "right"]:
        if is_legal_move(location, direction):
            can_move = True
            break
    return can_move  # Replace with code


def has_some_legal_move_somewhere(who):
    """
    Tests whether a legal move exists for player "who" (which must be either 'M' or 'R'). Does not provide any information on where the legal move is. You can assume that input will always be in correct range.
    """
    have_moves = False
    for location in all_locations():
        if at(location) == who:
            if can_move_piece_at(location):
                have_moves = True
                break
    return have_moves  # Replace with code


def possible_moves_from(location):
    """
    Returns a list of directions ('left', etc.) in which it is legal
    for the player at location to move. If there is no player at
    location, returns the empty list, [].
    You can assume that input will always be in correct range.
    """
    possible_moves = []
    if at(location) == "M":
        for direction in ["up", "down", "left", "right"]:
            if is_legal_move_by_musketeer(location, direction):
                possible_moves.append(direction)
    elif at(location) == "R":
        for direction in ["up", "down", "left", "right"]:
            if is_legal_move_by_enemy(location, direction):
                possible_moves.append(direction)
    return possible_moves  # Replace with code


def is_legal_location(location):
    """
    Tests if the location is legal on a 5x5 board.
    You can assume that input will always be in correct range.
    """
    is_legal = False
    if location[0] in range(5) and location[1] in range(5):
        is_legal = True
    return is_legal  # Replace with code


def is_within_board(location, direction):
    """
    Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range.
    """
    is_in_board = False
    row, col = adjacent_location(location, direction)
    if row in range(5) and col in range(5):
        is_in_board = True
    return is_in_board  # Replace with code


def all_possible_moves_for(player):
    """
    Returns every possible move for the player ('M' or 'R') as a list
    (location, direction) tuples.
    You can assume that input will always be in correct range.
    """
    player_moves = []
    for location in all_locations():
        if at(location) == player:
            for direction in possible_moves_from(location):
                if is_within_board(location, direction):
                    player_moves.append(((location), direction))
    return player_moves  # Replace with code


def make_move(location, direction):
    """
    Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range.
    """
    global board
    if at(location) == "M":
        board[location[0]][location[1]] = "-"
        new_row, new_col = adjacent_location(location, direction)
        board[new_row][new_col] = "M"
    elif at(location) == "R":
        board[location[0]][location[1]] = "-"
        new_row, new_col = adjacent_location(location, direction)
        board[new_row][new_col] = "R"
    return None  # Replace with code


def choose_computer_move(who):
    """
    The computer chooses a move for a Musketeer (who = 'M') or an enemy (who = 'R') and returns it as the tuple (location, direction), where a location is a (row, column) tuple as usual. You can assume that input will always be in correct range.
    """
    move_list = all_possible_moves_for(who)
    return move_list[0]  # Replace with code


def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    enemy_win = False
    mus_pos = []
    for loc in all_locations():
        if at(loc) == "M":
            mus_pos.append(loc)
    if mus_pos[0][0] == mus_pos[1][0] and mus_pos[1][0] == mus_pos[2][0]:
        enemy_win = True
    elif mus_pos[0][1] == mus_pos[1][1] and mus_pos[1][1] == mus_pos[2][1]:
        enemy_win = True
    return enemy_win  # Replace with code

# ---------- Communicating with the user ----------
# ----you do not need to modify code below unless you find a bug
# ----a bug in it before you move to stage 3


def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end=" ")
        for j in range(0, 5):
            print(board[i][j] + " ", end=" ")
        print()
        ch = chr(ord(ch) + 1)
    print()


def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()


def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user


def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L': 'left', 'R': 'right', 'U': 'up', 'D': 'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()


def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else:  # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)


def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else:  # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board


def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',
          location_to_string(location), 'to',
          location_to_string(new_location) + ".\n")


def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break


if __name__ == "__main__":
    start()
