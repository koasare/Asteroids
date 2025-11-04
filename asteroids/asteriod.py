import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Overrides the draw method to render the asteroid as a white circle.
        """
        # Draw a circle on the screen: (surface, color, center, radius, width)
        pygame.draw.circle(
            screen,
            "white",
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

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        # Calculate new velocities by rotating the current velocity
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)

        # Calculate the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        speed_factor = 1.2

        # Create the first new asteroid (uses Asteroid.containers automatically)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity_1 * speed_factor


        # Create the second new asteroid
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity_2 * speed_factor
        
