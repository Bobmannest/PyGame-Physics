import pygame
from pygame import Color
from Vertex import *
from screen import screen

pygame.init()

clock = pygame.time.Clock()

test_v = Vertex(pygame.Vector2(65, 65), 0, 0, 7)

running = True
while running:
    dt = clock.tick(30) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Color(174, 252, 252))

    test_v.gravity()
    test_v.update_position(dt)
    test_v.update_pointer()
    test_v.print_speed()

    pygame.display.flip()