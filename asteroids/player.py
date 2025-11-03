import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initializes the Player object.
        
        Args:
            x (int): Initial X center position.
            y (int): Initial Y center position.
        """
        # Call the parent class's constructor, passing in PLAYER_RADIUS for the hitbox
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def rotate(self, dt):
        """
        Checks for rotational input and calls the rotate method.
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Left rotation: Call rotate with negative dt to reverse direction
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Right rotation: Call rotate with positive dt
            self.rotate(dt)
        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # Move Backwards
            self.move(-dt)
    
    def move(self, dt):
        """
        Adjusts the player's position based on its current rotation, speed, and dt.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def triangle(self):
        """
        Calculates the three vertices of the player's ship (triangle)
        based on its position, radius, and current rotation.
        
        Returns:
            list: A list of pygame.Vector2 objects representing the triangle's points.
        """
        # A vector pointing forward (up)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # A vector pointing right (for the base corners)
        # Multiplied by radius/1.5 to adjust the triangle shape relative to the radius
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # Point A: The nose of the ship
        a = self.position + forward * self.radius
        
        # Point B: Bottom-left base corner
        b = self.position - forward * self.radius - right
        
        # Point C: Bottom-right base corner
        c = self.position - forward * self.radius + right
        
        return [a, b, c]
    
    def draw(self, screen):
        """
        Override the Circle Shape draw method to draw the triangle visual
        """
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
            )