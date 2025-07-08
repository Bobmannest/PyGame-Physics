import random

import pygame
from pygame import Color
from event import events_setup
from screen import screen, scr_width, scr_height
from ball import Ball

pygame.init()

clock = pygame.time.Clock()

balls = []
ball_count = 25
init = True


def biased_radius_generator():
    random_radius = random.randint(1, 8)
    if random_radius == 8:
        random_biased_radius = random.randint(10, 20)
    else:
        random_biased_radius = random.randint(7, 10)
    return random_biased_radius


while True:
    dt = clock.tick(30) / 1000
    if init:
        v = Ball(pygame.Vector2(100, 250), 0, 100, 0, 7, (168, 50, 50))
        balls.append(v)
        for _ in range(ball_count):
            # Creates balls with random stats
            random_x = random.randint(7, scr_width - 7)
            random_y = random.randint(7, scr_height - 7)
            random_x_velocity = random.randint(-300, 300)
            random_y_velocity = random.randint(-300, 300)
            direction = 0
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ball = Ball(
                pygame.Vector2(random_x, random_y),
                random_x_velocity,
                random_y_velocity,
                direction,
                biased_radius_generator(),
                random_color)
            balls.append(ball)
        init = False

    events_setup(balls)

    screen.fill(Color(174, 252, 252))
    for ball in balls:
        ball.check_collision(balls)
        ball.run(dt)
        #Optional stats monitoring methods
        #ball.velocity_pointer()
        #print('X:', ball.x_velocity, 'Y:', ball.y_velocity)
    pygame.display.flip()