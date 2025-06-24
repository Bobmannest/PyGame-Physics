import random
from pygame import Color
from event import events_setup
from box import *
from screen import screen, scr_width, scr_height

pygame.init()

clock = pygame.time.Clock()

balls = []
ball_count = 10
initialise = 0

while True:
    dt = clock.tick(30) / 1000

    if initialise == 0:
        v = Vertex(pygame.Vector2(100, 250), 1, 0, 0, 0, 7, (168, 50, 50))
        balls.append(v)
        for _ in range(ball_count):
            #Randomness
            rng_width = random.randint(7, scr_width - 7)
            rng_height = random.randint(7, scr_height - 7)
            rng_x = random.randint(-200, 200)
            rng_y = random.randint(-200, 200)
            # RNG that favours smaller balls
            rng_rad = random.randint(1, 8)
            if rng_rad == 8:
                rng_rad = random.randint(10, 20)
            else:
                rng_rad = random.randint(7, 10)
            rng_r = random.randint(0, 255)
            rng_g = random.randint(0, 255)
            rng_b = random.randint(0, 255)

            ball = Vertex(pygame.Vector2(rng_width, rng_height), 1, rng_x, rng_y, 0, rng_rad, (rng_r, rng_g, rng_b))

            balls.append(ball)
        initialise = 1

    events_setup(v, balls)

    screen.fill(Color(174, 252, 252))
    for ball in balls:
        ball.check_collision(balls)
        ball.run(dt)
        ball.velocity_pointer()

    pygame.display.flip()