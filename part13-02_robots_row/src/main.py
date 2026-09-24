# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
x = 0
repeat = 0

window.fill((0, 0, 0))

while x < 10:
    window.blit(robot, (50+repeat, 100))
    x += 1
    repeat += 50

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()