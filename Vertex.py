import pygame
from pygame import Vector2 as Vec2
from screen import screen, scr_height

#Colors
red = (168, 50, 50)
l_green = (144, 255, 144)

#Vertex is the planned name for the edge of the cube but for now its justa  ball shape
class Vertex:
    def __init__(self, center: Vec2, speed: int, direction: int, radius: int):
        self.center = center
        self.speed = speed
        self.direction = direction
        self.radius = radius

    #Gravity indefinitely increases the downwards speed
    def gravity(self):
        self.speed += 1

    #Updates ball position
    def update_position(self, dt):
        self.center.y += self.speed * dt
        pygame.draw.circle(screen, red, self.center, self.radius)

        if self.center.y >= (scr_height - self.radius):
            self.center.y = scr_height - self.radius
            self.speed = -self.speed
            self.speed //= 2

    #Pointer that shows direction of velocity but also the size of the line is the speed magnitude
    def update_pointer(self):
        pygame.draw.line(screen, l_green, self.center, (self.center.x, self.center.y + self.speed))

    def print_speed(self):
        print(self.speed)