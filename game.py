from snake import Snake
from geometry import OpenSquare

class Game:
    def __init__(self, *, food_num=0, rand_pos_generator=None, map_width=None, map_height=None):
        self.snake = Snake()
        self.rand_pos_generator = rand_pos_generator
        self.next_food_id_to_issue = 0
        if rand_pos_generator is not None:
            self.food_positions = [rand_pos_generator(n) for n in range(food_num)]
            self.next_food_id_to_issue = food_num
        else:
            self.food_positions = []
        self.map_width = map_width
        self.map_height = map_height

    def tick(self, n=1):
        for i in range(n):
            self.snake.advance_position()
            if self.snake.can_eat_food(self.get_food_positions()):
                self.eat_food_at(self.snake.get_head())

    def eat_food_at(self, position):
        self.snake.grow()
        self.remove_food_at(position)
        self.spawn_new_food()

    def remove_food_at(self, position):
        self.food_positions.remove(position)

    def spawn_new_food(self):
        self.food_positions.append(self.rand_pos_generator(self.next_food_id_to_issue))
        self.next_food_id_to_issue += 1

    def get_snake_positions(self):
        return self.snake.get_positions()

    def get_snake_velocity(self):
        return self.snake.get_velocity()

    def change_snake_velocity(self, relative_direction):
        self.snake.turn(relative_direction)

    def get_food_positions(self):
        return self.food_positions

    def is_over(self):
        map_area = OpenSquare(self.map_width, self.map_height)
        return (not map_area.includes(self.snake.get_head())) or self.snake.is_stepping_itself()
