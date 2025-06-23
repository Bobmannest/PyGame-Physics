import pygame
from pygame import Color

import event
from event import events_setup
from vertex import *
from screen import screen

pygame.init()

clock = pygame.time.Clock()

v1 = Vertex(pygame.Vector2(100, 250), 1, 0, 0, 0, 7)

while True:
    dt = clock.tick(30) / 1000

    events_setup(v1)

    screen.fill(Color(174, 252, 252))

    v1.run(dt)
    v1.velocity_pointer()
    v1.print_speed()

    pygame.display.flip()