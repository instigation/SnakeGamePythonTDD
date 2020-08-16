from vector import Vector
from utils import RelativeDirection


class Game:
    def __init__(self, *, food_num=1, rand_pos_generator=None):
        self.positions = [Vector(0, 0)] # head is always at index 0
        self.length = 1
        self.velocity = Vector(1, 0)
        self.rand_pos_generator = rand_pos_generator
        self.next_food_id_to_issue = 0
        if rand_pos_generator is not None:
            self.food_positions = [rand_pos_generator(n) for n in range(food_num)]
            self.next_food_id_to_issue = food_num
        else:
            self.food_positions = []

    def get_snake_head(self):
        return self.positions[0]

    def tick(self):
        self.advance_snake()
        if self.can_eat_food():
            self.eat_food_at(self.get_snake_head())

    def advance_snake(self):
        self.positions = [self.get_snake_head() + self.velocity] + self.positions[0:-1]

    def can_eat_food(self):
        return self.get_snake_head() in self.get_food_positions()

    def eat_food_at(self, position):
        self.grow_snake()
        self.remove_food_at(position)
        self.spawn_new_food()

    def grow_snake(self):
        self.positions.append(self.positions[-1] - Vector(1,0))

    def remove_food_at(self, position):
        self.food_positions.remove(position)

    def spawn_new_food(self):
        self.food_positions.append(self.rand_pos_generator(self.next_food_id_to_issue))
        self.next_food_id_to_issue += 1

    def get_snake_positions(self):
        return self.positions

    def get_snake_velocity(self):
        return self.velocity

    def change_snake_velocity(self, relative_direction):
        self.velocity = self.velocity.turn(relative_direction)

    def get_food_positions(self):
        return self.food_positions
