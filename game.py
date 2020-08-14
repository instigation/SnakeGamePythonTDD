from vector import Vector
from utils import RelativeDirection


class Game:
    def __init__(self, *, food_num=1, rand_pos_generator=None):
        self.positions = [Vector(0, 0)] # head is always at index 0
        self.length = 1
        self.velocity = Vector(1, 0)
        if rand_pos_generator is not None:
            self.food_positions = [rand_pos_generator(n) for n in range(food_num)]
        else:
            self.food_positions = []

    def get_snake_head(self):
        return self.positions[0]

    def tick(self):
        self.positions = [self.get_snake_head() + self.velocity] + self.positions[0:-1]
        if self.get_snake_head() in self.get_food_positions():
            self.positions.append(self.positions[-1] - Vector(1,0))

    def get_snake_positions(self):
        return self.positions

    def get_snake_velocity(self):
        return self.velocity

    def change_snake_velocity(self, relative_direction):
        self.velocity = self.velocity.turn(relative_direction)

    def get_food_positions(self):
        return self.food_positions
