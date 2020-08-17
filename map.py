from geometry import OpenSquare


class Map:
    def __init__(self, food_num, rand_pos_generator, map_width, map_height):
        assert ((food_num > 0) and (rand_pos_generator is not None)) or ((food_num == 0) and (rand_pos_generator is None))
        self.rand_pos_generator = rand_pos_generator
        self.next_food_id_to_issue = 0
        if rand_pos_generator is not None:
            self.food_positions = [rand_pos_generator(n) for n in range(food_num)]
            self.next_food_id_to_issue = food_num
        else:
            self.food_positions = []
        self.map_area = OpenSquare(map_width, map_height)

    def eat_food_at(self, position):
        self.remove_food_at(position)
        self.spawn_new_food()

    def remove_food_at(self, position):
        self.food_positions.remove(position)

    def spawn_new_food(self):
        self.food_positions.append(self.rand_pos_generator(self.next_food_id_to_issue))
        self.next_food_id_to_issue += 1

    def get_food_positions(self):
        return self.food_positions

    def not_includes(self, snake):
        return not self.map_area.includes(snake.get_head())
