from utils import RelativeDirection


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return 'Vector(x,y)'.replace('x', str(self.x)).replace('y', str(self.y))

    def l1_norm(self):
        return abs(self.x) + abs(self.y)

    def is_parallel_to(self, another_vector):
        return self.x*another_vector.y == self.y*another_vector.x

    def turn(self, relative_direction):
        turn_right = relative_direction == RelativeDirection.RIGHT
        turn_left = relative_direction == RelativeDirection.LEFT
        assert turn_right or turn_left
        if turn_right:
            return Vector(self.y, -self.x)
        elif turn_left:
            return Vector(-self.y, self.x)