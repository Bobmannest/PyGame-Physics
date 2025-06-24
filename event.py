import pygame
def events_setup(v, balls):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                ball.move_to_mouse()
