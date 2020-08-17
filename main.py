import pygame
from random import randint
from vector import Vector
from game import Game
from utils import RelativeDirection

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
SCALE = 20


def game_coordinate_to_screen_coordinate(game_coordinate_position):
    return (game_coordinate_position.scalar_multiply(SCALE) + Vector(DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)).to_list()


def draw_snake(snake_positions):
    for snake_position in snake_positions:
        pygame.draw.circle(screen, BLACK, game_coordinate_to_screen_coordinate(snake_position), SCALE//2, 0)


def draw_foods(food_positions):
    for food_position in food_positions:
        pygame.draw.circle(screen, BLUE, game_coordinate_to_screen_coordinate(food_position), SCALE//2)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('SnakeGameTDD')
    clock = pygame.time.Clock()

    map_width = DISPLAY_WIDTH//SCALE
    map_height = DISPLAY_HEIGHT//SCALE


    def pos_generator(n):
        return Vector(n*5+5,0)


    def rand_pos_generator(n):
        return Vector(randint(-map_width/2+1, map_width/2-1), randint(-map_height/2+1, map_height/2-1))


    game = Game(food_num=4, rand_pos_generator=rand_pos_generator, map_width=map_width, map_height=map_height)

    user_exited = False
    while not user_exited:
        if game.is_over():
            print('Game Over!')
            break

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                user_exited = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.change_snake_velocity(RelativeDirection.LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.change_snake_velocity(RelativeDirection.RIGHT)

        screen.fill(WHITE)
        draw_snake(game.get_snake_positions())
        draw_foods(game.get_food_positions())

        pygame.display.update()
        clock.tick(5)
        game.tick()