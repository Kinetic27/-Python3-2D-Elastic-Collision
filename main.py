from sys import exit

import pygame
from pygame.locals import *
from box import Box
from vector import Vector2
from world import World
from random import *

SCREEN_LENGTH = 580
SCREEN_WIDTH = 840
NUMBER_OF_BALLS = 2


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH), 0, 32)
    world = World(SCREEN_LENGTH, SCREEN_WIDTH)

    world.add_ball(Box(Vector2(200, 200), Vector2(0, 0), 50, 1,
                       (randint(0, 255), randint(0, 255), randint(0, 255))))

    world.add_ball(Box(Vector2(600, 200), Vector2(-100, 0), 100, 10000,
                       (randint(0, 255), randint(0, 255), randint(0, 255))))

    clock = pygame.time.Clock()

    # Game loop:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        time_passed_seconds = clock.tick() / 1000.0
        world.update(time_passed_seconds)
        world.render(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
