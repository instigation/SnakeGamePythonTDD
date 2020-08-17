from vector import Vector


class Snake:
    def __init__(self):
        self.positions = [Vector(0, 0)] # head is always at index 0
        self.last_tail_position = None
        self.velocity = Vector(1, 0)

    def get_head(self):
        return self.positions[0]

    def advance_position(self):
        self.last_tail_position = self.positions[-1]
        self.positions = [self.get_head() + self.velocity] + self.positions[0:-1]

    def grow(self):
        if self.last_tail_position is None:
            print('Should call advance_position before calling grow')
            self.last_tail_position = Vector(0,-1)
        self.positions.append(self.last_tail_position)

    def turn(self, relative_direction):
        self.velocity = self.velocity.turn(relative_direction)

    def can_eat_food(self, food_positions):
        return self.get_head() in food_positions

    def is_stepping_itself(self):
        return len(self.positions) != len(set(self.positions))

    def get_positions(self):
        return self.positions

    def get_velocity(self):
        return self.velocity