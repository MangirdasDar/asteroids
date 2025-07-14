import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.width = 2
        
        # Should I add self. next to arguments below?
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            self.velocity.rotate(random_angle, -random_angle)
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.radius)
            self.velocity(self.radius) * 1.2
            Asteroid(self.radius)
            self.velocity(self.radius) * 1.2
            
