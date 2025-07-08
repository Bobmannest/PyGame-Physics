import math
import pygame

from pygame import Vector2 as Vec2
from screen import screen, scr_height, scr_width

green = (0, 255, 0)


class Ball:
    gravity = 10
    air_res = 1
    bounciness = 0.2
    friction = 0.8
    mouse_follow_intensity = 1

    def __init__(self, center: Vec2, x_velocity: int, y_velocity: int, direction: int, radius: int, color: tuple):
        self.center = center
        # Mass is equal to πr^2 since im keeping density constant
        self.mass = int(0.08 * (radius ^ 2) * math.pi)
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.direction = direction
        self.radius = radius
        self.color = color

    # Gravity indefinitely increases the downwards speed. 10(9.81 rounded) is too large, so I went with 1 instead
    def run(self, dt):
        #Gravity(mg)
        self.y_velocity += self.mass * Ball.gravity

        # Horizontal air resistance
        if self.x_velocity > 0:
            self.x_velocity -= self.air_res
        elif self.x_velocity < 0:
            self.x_velocity += self.air_res

        # Updates ball position
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
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def check_collision(self, balls):
        for ball in balls:
            dx = self.center.x - ball.center.x
            dy = self.center.y - ball.center.y
            distance = math.hypot(dx, dy)

            if distance <= self.radius + ball.get_radius():
                if dx > 0:
                    self.center.x += 1
                    self.x_velocity = int(Ball.friction * abs(self.x_velocity))
                elif dx < 0:
                    self.center.x -= 1
                    self.x_velocity = int(Ball.friction * -abs(self.x_velocity))
                if dy > 0:
                    self.center.y += 1
                    self.y_velocity = abs(self.y_velocity)
                    self.y_velocity //= 2
                elif dy < 0:
                    self.center.y -= 1
                    self.y_velocity = -abs(self.y_velocity)
                    self.y_velocity //= 2

    def move_to_mouse(self):
        x, y = pygame.mouse.get_pos()
        self.x_velocity = int(x - self.center.x) * Ball.mouse_follow_intensity
        self.y_velocity = int(y - self.center.y) * Ball.mouse_follow_intensity

    def velocity_line(self):
        pygame.draw.line(screen, green, self.center, (self.center.x + self.x_velocity, self.center.y + self.y_velocity))

    def print_speed(self):
        print('H:', self.x_velocity, 'V:', self.y_velocity)

    def get_center(self):
        return self.center

    def get_radius(self):
        return self.radius

    def add_center_x(self, add):
        self.center.x += add

    def add_center_y(self, add):
        self.center.y += add
