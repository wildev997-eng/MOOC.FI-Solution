# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame


pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
y = 0

window.fill((0, 0, 0))

while y < 1000:
    window.blit(robot, (randint(1,640-width), randint(1,480-height)))
    y += 1

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()