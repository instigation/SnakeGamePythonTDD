from vector import Vector


class OpenSquare:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def includes(self, vector):
        if (self.width is None) or (self.height is None):
            return True
        return (abs(vector.x)*2 < self.width) and (abs(vector.y) < self.height)
