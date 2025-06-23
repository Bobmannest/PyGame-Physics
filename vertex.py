import pygame
from pygame import Vector2 as Vec2
from screen import screen, scr_height, scr_width

#Colors
red = (168, 50, 50)
green = (0, 255, 0)

#Vertex is the planned name for the edge of the cube but for now its justa  ball shape
class Vertex:
    air_res = 1
    def __init__(self, center: Vec2, mass: int, x_velocity: int, y_velocity: int, direction: int, radius: int):
        self.center = center
        self.mass = mass
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.direction = direction
        self.radius = radius

    #Gravity indefinitely increases the downwards speed. 10(9.81 rounded) is too large, so I went with 1 instead
    def run(self, dt):
        #Gravity(mg)
        self.y_velocity += self.mass * 10

        #Horizontal air resistance
        if self.x_velocity > 0:
            self.x_velocity -= self.air_res
        elif self.x_velocity < 0:
            self.x_velocity += self.air_res

        #Updates ball position
        self.center.x += self.x_velocity * dt
        self.center.y += self.y_velocity * dt

        # Checks ball does not go off bounds(X plane)
        if self.center.x > (scr_width - self.radius):
            self.center.x = scr_width - self.radius
            self.x_velocity = -self.x_velocity
        elif self.center.x < (0 + self.radius):
            self.center.x = 0 + self.radius
            self.x_velocity = -self.x_velocity

        # Checks ball does not go off bounds(Y plane)
        if self.center.y > (scr_height - self.radius):
            self.center.y = scr_height - self.radius
            self.y_velocity = -self.y_velocity
            self.y_velocity //= 2
        elif self.center.y < (0 + self.radius):
            self.center.y = 0 + self.radius
            self.y_velocity = -self.y_velocity

        #Draws the circle
        pygame.draw.circle(screen, red, self.center, self.radius)

    def move_to_mouse(self):
        x, y = pygame.mouse.get_pos()
        self.x_velocity = x - self.center.x
        self.y_velocity = y - self.center.y

    #Pointer that shows direction of velocity but also the size of the line is the speed magnitude
    def velocity_pointer(self):
        pygame.draw.line(screen, green, self.center, (self.center.x + self.x_velocity, self.center.y + self.y_velocity))

    def print_speed(self):
        print('H:', self.x_velocity, 'V:', self.y_velocity)