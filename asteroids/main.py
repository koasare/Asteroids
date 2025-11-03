# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteriod import Asteroid # Import the new Asteroid class
from asteroidfield import AsteroidField

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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

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
            if player.collision(asteroid):
                print("Game over!")
                running = False # Exit the game loop
                break # Immediately stop checking and exit the game loop

        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(240) / 1000
        
    pygame.quit()


if __name__ == "__main__":
    main()
