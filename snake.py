from vector import Vector


class Snake:
    def __init__(self):
        self.positions = [Vector(0, 0)] # head is always at index 0
        self.velocity = Vector(1, 0)

    def get_head(self):
        return self.positions[0]

    def advance_position(self):
        self.positions = [self.get_head() + self.velocity] + self.positions[0:-1]

    def grow(self):
        self.positions.append(self.positions[-1] - Vector(1, 0))

    def turn(self, relative_direction):
        self.velocity = self.velocity.turn(relative_direction)

    def can_eat_food(self, food_positions):
        return self.get_head() in food_positions

    def get_positions(self):
        return self.positions

    def get_velocity(self):
        return self.velocity