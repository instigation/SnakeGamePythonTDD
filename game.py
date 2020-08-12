from vector import Vector


class Game:
    def __init__(self):
        self.position = Vector(0, 0)

    def tick(self):
        self.position += Vector(0, 1)

    def get_snake_positions(self):
        return [self.position]