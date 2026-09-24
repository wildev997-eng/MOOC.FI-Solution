# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

x1, y1 = 0, 0
x2, y2 = 300, 0

p1_right = p1_left = p1_up = p1_down = False
p2_right = p2_left = p2_up = p2_down = False

clock = pygame.time.Clock()

def player_1(image, x, y):
    window.blit(image, (x, y))
    

def player_2(image, x, y):
    window.blit(image, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1_left = True
            if event.key == pygame.K_RIGHT:
                p1_right = True
            if event.key == pygame.K_UP:
                p1_up = True
            if event.key == pygame.K_DOWN:
                p1_down = True
            
            if event.key == pygame.K_a:
                p2_left = True
            if event.key == pygame.K_d:
                p2_right = True
            if event.key == pygame.K_w:
                p2_up = True
            if event.key == pygame.K_s:
                p2_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1_left = False
            if event.key == pygame.K_RIGHT:
                p1_right = False
            if event.key == pygame.K_UP:
                p1_up = False
            if event.key == pygame.K_DOWN:
                p1_down = False

            if event.key == pygame.K_a:
                p2_left = False
            if event.key == pygame.K_d:
                p2_right = False
            if event.key == pygame.K_w:
                p2_up = False
            if event.key == pygame.K_s:
                p2_down = False
        
        if event.type == pygame.QUIT:
            exit()

    if p1_right and x1 + width < 640:
        x1 += 2
    if p1_left and x1 > 0:
        x1 -= 2
    if p1_up and y1 > 0:
        y1 -= 2
    if p1_down and y1 + height < 480:
        y1 += 2

    if p2_right and x2 + width < 640:
        x2 += 2
    if p2_left and x2 > 0:
        x2 -= 2
    if p2_up and y2 > 0:
        y2 -= 2
    if p2_down and y2 + height < 480:
        y2 += 2

    window.fill((0, 0, 0))
    player_1(robot, x1, y1)
    player_2(robot, x2, y2)
    pygame.display.flip()

    clock.tick(60)