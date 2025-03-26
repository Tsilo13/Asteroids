import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        old_radius = self.radius

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            p_vector = self.velocity.rotate(random_angle) * 1.2
            n_vector = self.velocity.rotate(-random_angle) * 1.2
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid_child1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_child1.velocity = p_vector * 1.2
            asteroid_child2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_child2.velocity = n_vector * 1.2
