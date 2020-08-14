import pytest
from game import Game
from vector import Vector
from utils import RelativeDirection

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
    delta_position = new_snake_positions[0] - original_snake_positions[0]
    assert delta_position.l1_norm() == 1

def test_snake_should_follow_velocity_direction():
    game = Game()
    original_snake_positions = game.get_snake_positions()
    snake_velocity = game.get_snake_velocity()
    game.tick()
    new_snake_positions = game.get_snake_positions()
    assert len(original_snake_positions) > 0
    assert len(new_snake_positions) > 0
    delta_position = new_snake_positions[0] - original_snake_positions[0]
    assert snake_velocity.is_parallel_to(delta_position)

def test_snake_initial_velocity_should_be_towards_positive_x_axis():
    game = Game()
    snake_velocity = game.get_snake_velocity()
    assert snake_velocity == Vector(1,0)

@pytest.mark.parametrize('relative_direction', [RelativeDirection.RIGHT, RelativeDirection.LEFT])
def test_snake_velocity_should_change(relative_direction):
    game = Game()
    original_snake_velocity = game.get_snake_velocity()
    game.change_snake_velocity(relative_direction)
    new_snake_velocity = game.get_snake_velocity()
    assert original_snake_velocity.turn(relative_direction) == new_snake_velocity

def test_game_random_generates_foods():

    def rand_pos_generator(n):
        return Vector(n+1,n+1)

    game = Game(food_num=1, rand_pos_generator=rand_pos_generator)
    food_positions = game.get_food_positions()
    assert len(food_positions) == 1
    assert food_positions[0] == Vector(1,1)

def test_snake_gets_longer_by_eating_foods():

    def rand_pos_generator(n):
        y = 2 if n%2 == 0 else -2
        return Vector(y,0)

    game = Game(food_num=1, rand_pos_generator=rand_pos_generator)
    assert game.get_snake_velocity() == Vector(1,0)
    game.tick()
    game.tick()
    snake_positions = game.get_snake_positions()
    assert len(snake_positions) == 2

def test_snake_turn_gradually_turns_its_body():

    def rand_pos_generator(n):
        return Vector(n+1,0)

    game = Game(food_num=2, rand_pos_generator=rand_pos_generator)
    assert game.get_snake_velocity() == Vector(1,0)
    game.tick()
    game.tick()
    assert set(game.get_snake_positions()) == {Vector(0,0), Vector(1,0), Vector(2,0)}
    game.change_snake_velocity(RelativeDirection.RIGHT)
    game.tick()
    assert set(game.get_snake_positions()) == {Vector(1,0), Vector(2,0), Vector(2,-1)}
    game.tick()
    assert set(game.get_snake_positions()) == {Vector(2,0), Vector(2,-1), Vector(2,-2)}
