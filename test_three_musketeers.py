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


def test_set_board():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((1, 3)) == M
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
    assert len(locations) == 25


def test_adjacent_location():
    # Replace with tests
    assert adjacent_location((0, 0), right) == (0, 1)


def test_is_legal_move_by_musketeer():
    # Replace with tests
    assert is_legal_move_by_musketeer((1, 3), up) == False


def test_is_legal_move_by_enemy():
    # Replace with tests
    assert is_legal_move_by_enemy((2, 2), up) == False


def test_is_legal_move():
    # Replace with tests
    t_location = (0, 3)
    t_direction = down
    if at(t_location) == 'M':
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
    assert possible_moves_from((1, 3)) == [left, down]


def test_is_legal_location():
    # Replace with tests
    assert is_legal_location((2, 3)) == True


def test_is_within_board():
    # Replace with tests
    assert is_within_board((1, 3), down) == True


def test_all_possible_moves_for():
    # Replace with tests
    assert all_possible_moves_for(
        'M') == [((1, 3), 'down'), ((1, 3), 'left'), ((2, 2), 'left')]


def test_make_move():
    # Replace with tests
    assert make_move((1, 3), down) == (2, 3)


def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'
    assert choose_computer_move('M') == ((1, 2), left)


def test_is_enemy_win():
    # Replace with tests
    assert is_enemy_win() == True
