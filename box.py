from math import hypot

import pygame
from pygame import Vector2 as Vec2
from screen import screen
from vertex import Vertex

red = (168, 50, 50)
yellow = (255, 224, 66)
green = (103, 255, 61)
blue = (50, 102, 168)
black = (45, 43, 46)

#Creates a Box with height and width of 50px
class Box:
    rigidness = 1
    def __init__(self, dt, center: Vec2, width):
        self.center = center
        self.dt = dt
        self.width = width

        #Square points(1 - red, 2 - yellow, 3 - green, 4 - blue)
        self.v1 = Vertex(pygame.Vector2(self.center), 1, 0, 0, 0, 7, red)
        self.v2 = Vertex(pygame.Vector2(self.center.x + self.width, self.center.y), 1, 0, 0, 0, 7, yellow)
        self.v3 = Vertex(pygame.Vector2(self.center.x + self.width, self.center.y + self.width), 1, 0, 0, 0, 7, green)
        self.v4 = Vertex(pygame.Vector2(self.center.x, self.center.y + self.width), 1, 0, 0, 0, 7, blue)

    #a mess
    def maintain_shape(self, current: Vertex, other: Vertex):
        dx = int(current.get_center().x - other.get_center().x)
        dy = int(current.get_center().y - other.get_center().y)

        distance = hypot(dx, dy)
        if distance < self.width:
            if dy < 0:
                current.add_center_y(-(self.width-abs(dy)))
            elif dy > 0:
                current.add_center_y(self.width-abs(dy))

    def run(self):
        pygame.draw.line(screen, black, self.v1.get_center(), self.v2.get_center(), 5)
        pygame.draw.line(screen, black, self.v2.get_center(), self.v3.get_center(), 5)
        pygame.draw.line(screen, black, self.v3.get_center(), self.v4.get_center(), 5)
        pygame.draw.line(screen, black, self.v4.get_center(), self.v1.get_center(), 5)

        self.v1.run(self.dt)
        self.v2.run(self.dt)
        self.v3.run(self.dt)
        self.v4.run(self.dt)

        self.maintain_shape(self.v1, self.v2)
        self.maintain_shape(self.v1, self.v4)

        self.maintain_shape(self.v3, self.v2)
        self.maintain_shape(self.v3, self.v4)




