from snake import Snake
from map import Map

class Game:
    def __init__(self, *, food_num=0, rand_pos_generator=None, map_width=None, map_height=None):
        self.snake = Snake()
        self.map = Map(food_num, rand_pos_generator, map_width, map_height)

    def tick(self, n=1):
        for i in range(n):
            self.snake.advance_position()
            if self.snake.can_eat_food(self.get_food_positions()):
                self.eat_food_at(self.snake.get_head())

    def eat_food_at(self, position):
        self.snake.grow()
        self.map.eat_food_at(position)

    def get_snake_positions(self):
        return self.snake.get_positions()

    def get_snake_velocity(self):
        return self.snake.get_velocity()

    def change_snake_velocity(self, relative_direction):
        self.snake.turn(relative_direction)

    def get_food_positions(self):
        return self.map.get_food_positions()

    def is_over(self):
        return self.map.not_includes(self.snake) or self.snake.is_stepping_itself()
