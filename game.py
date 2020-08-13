from vector import Vector
from utils import RelativeDirection


class Game:
    def __init__(self):
        self.position = Vector(0, 0)
        self.velocity = Vector(1, 0)

    def tick(self):
        self.position += Vector(1, 0)

    def get_snake_positions(self):
        return [self.position]

    def get_snake_velocity(self):
        return self.velocity

    def change_snake_velocity(self, relative_direction):
        self.velocity = self.velocity.turn(relative_direction)