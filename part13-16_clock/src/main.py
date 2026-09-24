import pygame
import math
from datetime import datetime

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

CENTER = (320, 240)
RADIUS = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    now = datetime.now()
    pygame.display.set_caption(now.strftime("%H:%M:%S"))

    minute_fraction = now.minute / 60
    hour_fraction = (now.hour % 12) / 12 + now.minute / (12 * 60)
    second_fraction = now.second / 60

    minute_angle = minute_fraction * 2 * math.pi - math.pi / 2
    hour_angle = hour_fraction * 2 * math.pi - math.pi / 2
    second_angle = second_fraction * 2 * math.pi - math.pi / 2

    minute_length = RADIUS * 0.8
    hour_length = RADIUS * 0.5
    second_length = RADIUS * 0.9

    minute_x = CENTER[0] + math.cos(minute_angle) * minute_length
    minute_y = CENTER[1] + math.sin(minute_angle) * minute_length

    hour_x = CENTER[0] + math.cos(hour_angle) * hour_length
    hour_y = CENTER[1] + math.sin(hour_angle) * hour_length

    second_x = CENTER[0] + math.cos(second_angle) * second_length
    second_y = CENTER[1] + math.sin(second_angle) * second_length

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 0, 0), CENTER, RADIUS, 3)
    pygame.draw.line(window, (0, 0, 255), CENTER, (minute_x, minute_y), 2)
    pygame.draw.line(window, (0, 0, 255), CENTER, (hour_x, hour_y), 4)
    pygame.draw.line(window, (0, 255, 0), CENTER, (second_x, second_y), 1)
    pygame.draw.circle(window, (255, 0, 0), CENTER, 8)
    pygame.display.flip()

    clock.tick(60)