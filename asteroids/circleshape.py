import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        """
        Checks for collision between this CircleShape and another CircleShape object.
        Collision occurs if the distance between centers is less than or equal to 
        the sum of their radii (r1 + r2).
        """
        # Calculate the distance between the two centers (position is a Vector2)
        distance = self.position.distance_to(other.position)

        # Collision occurs if the distance is less than or equal to the sum of radii
        min_distance = self.radius + other.radius

        return distance <= min_distance

