# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
y = 0
repeat = 0
start_width = 50
start_height = 100

window.fill((0, 0, 0))

while y < 10:
    repeat = 0
    for x in range(10):
        window.blit(robot, (start_width + repeat, start_height))
        repeat += 40
    start_width += 10
    start_height += 20
    y += 1

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()