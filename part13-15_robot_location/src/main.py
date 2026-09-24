import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = randint(1, 640 - robot.get_width())
            y = randint(1, 480 - robot.get_height())

            window.fill((0, 0, 0))
            window.blit(robot, (x, y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()