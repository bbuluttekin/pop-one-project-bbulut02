import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 = [[_, _, _, M, _],
          [_, _, R, M, _],
          [_, R, M, R, _],
          [_, R, _, _, _],
          [_, _, _, R, _]]


def test_create_board():
    create_board()
    assert at((0, 0)) == R
    assert at((0, 4)) == M
    # eventually add at least two more test cases
    assert at((4, 0)) == M
    assert at((4, 4)) == R


def test_set_board():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((1, 3)) == M
    assert at((1, 0)) == "-"
    # eventually add some board2 and at least 3 tests with it


def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    # eventually add at least one more test with another board


def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0, 0)
    # eventually add at least one more exception test and two more
    # test with correct inputs
    with pytest.raises(ValueError):
        string_to_location("A9")
    assert string_to_location("E1") == (4, 0)
    assert string_to_location("B5") == (1, 4)


def test_location_to_string():
    # Replace with tests
    assert location_to_string((0, 1)) == "A2"
    with pytest.raises(ValueError):
        location_to_string((6, 6))


def test_at():
    # Replace with tests
    assert at((0, 3)) == M


def test_all_locations():
    # Replace with tests
    locations = []
    for i in range(0, 5):
        for j in range(0, 5):
            locations.append((i, j))
    assert all_locations() == locations
    assert len(all_locations()) == 25


def test_adjacent_location():
    # Replace with tests
    assert adjacent_location((0, 0), right) == (0, 1)
    assert adjacent_location((1, 2), up) == (0, 2)


def test_is_legal_move_by_musketeer():
    # Replace with tests
    assert is_legal_move_by_musketeer((1, 3), up) == False


def test_is_legal_move_by_enemy():
    # Replace with tests
    assert is_legal_move_by_enemy((2, 1), up) == True
    assert is_legal_move_by_enemy((2, 1), right) == False


def test_is_legal_move():
    # Replace with tests
    t_location = (1, 3)
    t_direction = down
    if board1[t_location[0]][t_location[1]] == 'M':
        assert is_legal_move_by_musketeer(t_location, t_direction) == True
    else:
        assert is_legal_move_by_enemy(t_location, t_direction) == True


def test_can_move_piece_at():
    # Replace with tests
    assert can_move_piece_at((1, 3)) == True


def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board


def test_possible_moves_from():
    # Replace with tests
    assert 'left' in possible_moves_from((1, 3))
    assert 'down' in possible_moves_from((1, 3))
    assert "up" not in possible_moves_from((1, 3))
    assert "up" in possible_moves_from((1, 2))
    assert "left" in possible_moves_from((1, 2))
    assert "up" in possible_moves_from((2, 1))
    assert "left" in possible_moves_from((2, 1))


def test_is_legal_location():
    # Replace with tests
    assert is_legal_location((2, 3)) == True
    assert is_legal_location((5, 1)) == False


def test_is_within_board():
    # Replace with tests
    assert is_within_board((1, 3), down) == True
    assert is_within_board((4, 4), right) == False


def test_all_possible_moves_for():
    # Replace with tests
    m_moves = [
        ((1, 3), down),
        ((1, 3), left),
        ((2, 2), left),
        ((2, 2), right)
    ]
    r_moves = [
        ((1, 2), up),
        ((1, 2), left),
        ((2, 1), up),
        ((2, 1), left)
    ]
    for move in r_moves:
        assert move in all_possible_moves_for("R")
    for item in m_moves:
        assert item in all_possible_moves_for("M")


def test_make_move():
    # Replace with tests
    t_player = at((1, 3))
    make_move((1, 3), down)
    assert at(adjacent_location((1, 3), down)) == t_player


def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'
    #assert choose_computer_move('M') == ((1, 3), down)
    assert choose_computer_move("R") == ((1, 2), up)


def test_is_enemy_win():
    # Replace with tests
    assert is_enemy_win() == False
