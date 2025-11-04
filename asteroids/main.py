# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteriod import Asteroid # Import the new Asteroid class
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Kwesi's Asteroids")

    clock = pygame.time.Clock()
    dt = 0

    # Group for objects that need an update call (Player, Asteroids, Bullets)
    updatable = pygame.sprite.Group()
    # Group for objects that need a draw call (Player, Asteroids, Bullets)
    drawable = pygame.sprite.Group()
    # Group for objects that need a draw call (Player, Asteroids, Bullets)
    asteroids = pygame.sprite.Group()
    # Group for objects that need a draw call (Player, Asteroids, Bullets)
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # 4. Instantiate the Player object ✨
    # x and y are passed to the constructor to spawn the player in the middle.
    player = Player(
        x = SCREEN_WIDTH / 2,
        y = SCREEN_HEIGHT / 2
    )

    field = AsteroidField()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)

        for asteroid in asteroids:
            asteroid_destroyed = False
            
            # 1. Shot-Asteroid check
            for shot in shots:
                if shot.collides_with(asteroid):
                    # Remove both objects from all groups
                    shot.kill()
                    asteroid.split()
                    asteroid_destroyed = True
                    # Break the inner (shots) loop and move to player check
                    break 

            # If the asteroid was destroyed by a shot, skip the player collision check
            if asteroid_destroyed:
                continue 

            # 2. Player-Asteroid check
            if player.collides_with(asteroid):
                print("Game over!")
                running = False 
                break # Exit the main asteroid loop and end the game
        # ------------------------------------

        screen.fill((0,0,0))

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(240) / 1000
        
    pygame.quit()


if __name__ == "__main__":
    main()
