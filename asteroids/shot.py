import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """
        Overrides the draw method to render the asteroid as a white circle.
        """
        # Draw a circle on the screen: (surface, color, center, radius, width)
        pygame.draw.circle(
            screen,
            "green",
            self.position,
            self.radius,
            2 # Line width of 2
        )
    
    def update(self, dt):
        """
        Overrides the update method to move the asteroid in a straight line.
        """
        # Add (velocity * dt) to the current position to move the object
        self.position += self.velocity * dt