import pygame
from constants import *
from CircleShape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        print("shot drawn")
    def update(self, dt):
        self.position += self.velocity * dt
        print("shot updated")