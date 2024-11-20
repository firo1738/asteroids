from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(split_angle)
            v2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            A1 = Asteroid(self.position.x, self.position.y, new_radius)
            A2 = Asteroid(self.position.x, self.position.y, new_radius)
            A1.velocity = v1*1.2
            A2.velocity = v2*1.2
