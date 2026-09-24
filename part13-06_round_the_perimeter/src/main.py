import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

switch = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if switch:
        x += velocity
    else:
        y += velocity

    if switch and velocity > 0 and x+robot.get_width() >= 640:
        switch = False
    
    if not switch and velocity > 0 and y+robot.get_height() >= 480:
        velocity = -velocity
        switch = True
    
    if velocity < 0 and x <= 0:
        switch = False

    if velocity < 0 and y <= 0:
        velocity = -velocity
        switch = True  

    clock.tick(60)