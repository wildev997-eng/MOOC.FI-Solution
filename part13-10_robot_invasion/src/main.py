import pygame
from random import randint, choice, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

velocity = 1
slide_velocity = 2
spawn_chance = 0.02

robots = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if random() < spawn_chance:
        robots.append({
            "x": randint(1, 640 - width),
            "y": -100,
            "state": "falling",
            "slide_direction": None
        })

    for bot in robots:
        if bot["state"] == "falling":
            bot["y"] += velocity
            if bot["y"] + height >= 480:
                bot["y"] = 480 - height
                bot["state"] = "sliding"
                bot["slide_direction"] = choice([-1, 1])
        elif bot["state"] == "sliding":
            bot["x"] += slide_velocity * bot["slide_direction"]

    robots = [bot for bot in robots if not (bot["state"] == "sliding" and (bot["x"] + width < 0 or bot["x"] > 640))]

    window.fill((0, 0, 0))
    for bot in robots:
        window.blit(robot, (bot["x"], bot["y"]))
    pygame.display.flip()

    clock.tick(60)