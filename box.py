import pygame
from pygame import Vector2 as Vec2
from screen import screen

red = (168, 50, 50)
yellow = (255, 224, 66)
green = (103, 255, 61)
blue = (50, 102, 168)
black = (45, 43, 46)

#Creates a Box with height and width of 50px
class Box:
    def __init__(self, center: Vec2, speed: int, direction: int, rotation: int):
        self.center = center
        self.speed = speed
        self.direction = direction
        self.rotation = rotation

        # Square points(1 - red, 2 - yellow, 3 - green, 4 - blue)
        v1 = pygame.Vector2(center.x-24.5, center.y-24.5)
        v2 = pygame.Vector2(center.x+24.5, center.y-24.5)
        v3 = pygame.Vector2(center.x+24.5, center.y+24.5)
        v4 = pygame.Vector2(center.x-24.5, center.y+24.5)

        pygame.draw.line(screen, black, v1, v2, 5)
        pygame.draw.line(screen, black, v2, v3, 5)
        pygame.draw.line(screen, black, v3, v4, 5)
        pygame.draw.line(screen, black, v4, v1, 5)

        pygame.draw.circle(screen, red, v1, 7)
        pygame.draw.circle(screen, yellow, v2, 7)
        pygame.draw.circle(screen, green, v3, 7)
        pygame.draw.circle(screen, blue, v4, 7)

    def gravity(self):
        self.speed += 0.01

    def update_position(self):
        self.center.y += self.speed