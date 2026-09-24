import pygame
from random import randint, choice, random

pygame.init()
window = pygame.display.set_mode((640, 480))
game_font = pygame.font.SysFont("Arial", 24)


rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png")
width_rock = rock.get_width()
height_rock = rock.get_height()
width_robot = robot.get_width()
height_robot = robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

velocity = 1
spawn_chance = 0.01
x = 0
y = 480 - height_robot
score = 0


rocks = []

clock = pygame.time.Clock()

restart = True

while True:
    rect_robot = robot.get_rect(topleft=(x, 480 - height_robot))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()
    
    if to_right and x + width_robot < 640:
        x += 2
    if to_left and x > 0:
        x -= 2

    if not restart:
        break

    if random() < spawn_chance:
        rocks.append({
            "x": randint(1, 640 - width_rock),
            "y": -100,
            "state": "falling",
            "slide_direction": None
        })

    for bot in rocks:
        if bot["state"] == "falling":
            bot["y"] += velocity
            if bot["y"] + height_rock >= 480:
                bot["y"] = 480 - height_rock
                restart = False

        rect_rock = rock.get_rect(topleft=(bot["x"], bot["y"]))

        if rect_robot.colliderect(rect_rock):
            score += 1
            bot["state"] = "hit"
    
    rocks = [bot for bot in rocks if bot["state"] != "hit"]

    text = game_font.render(f"Points: {score}", True, (255, 0, 0))
    
    window.fill((0, 0, 0))
    for bot in rocks:
        window.blit(rock, (bot["x"], bot["y"]))
    
    window.blit(robot, (x, 480 - height_robot))
    window.blit(text, (500, 0))


    pygame.display.flip()

    clock.tick(60)