import pytest
from game import Game


def test_initial_snake_should_be_size_one():
    game = Game()
    snake_positions = game.get_snake_positions()
    assert len(snake_positions) == 1


def test_snake_should_advance_over_time():
    game = Game()
    original_snake_positions = game.get_snake_positions()
    game.tick()
    new_snake_positions = game.get_snake_positions()
    assert original_snake_positions != new_snake_positions

def test_snake_speed_should_be_one():
    game = Game()
    original_snake_positions = game.get_snake_positions()
    game.tick()
    new_snake_positions = game.get_snake_positions()
    assert len(original_snake_positions) > 0
    assert len(new_snake_positions) > 0
    moved_distance = new_snake_positions[0] - original_snake_positions[0]
    assert moved_distance.l1_norm() == 1