🚀 Pygame Asteroids Clone (In Development)

This is a foundation project for a classic arcade-style Asteroids clone built using Pygame. The core game loop, entity management, player movement, shooting, and asteroid splitting mechanics are currently implemented.

🕹️ Current Features

The game is currently focused on establishing core physics and object interaction:

Player Control: Full rotational and thrust-based movement using vector physics and delta time (dt) for smooth, frame-rate independent motion.

Projectile System: Player can fire laser shots with a built-in cooldown mechanism.

Asteroid Management:

Asteroids spawn dynamically from the edges of the screen.

When an asteroid is hit by a bullet, it splits into two smaller, faster asteroids, introducing the core challenge mechanic.

Smallest asteroids are destroyed upon collision.

Collision Detection: Uses accurate circle-to-circle collision checks for all game entities (Player-Asteroid, Shot-Asteroid).

Game End: The game immediately terminates upon player collision with any asteroid.

Object Groups: Utilizes pygame.sprite.Group for efficient updating and drawing of all game entities (player, asteroids, and shots).

🎮 How to Play

Controls

Key

Action

W

Thrust Forward (Accelerate)

S

Thrust Backward (Decelerate/Reverse)

A

Rotate Left

D

Rotate Right

Space

Fire Shot (Subject to Cooldown)

Close Button

Exit Game

Collision Rules

Shot vs. Asteroid: Asteroid splits (or is destroyed if small enough), and the shot is destroyed.

Player vs. Asteroid: Game over.

⚙️ Project Structure Overview

File

Description

main.py

Initializes Pygame, sets up the game loop, instantiates groups and the AsteroidField, and handles all collision logic.

circleshape.py

Base class (pygame.sprite.Sprite extension) for all circular entities (Player, Asteroid, Shot). Contains vector-based position/velocity and the fundamental collides_with() method.

player.py

Defines the player ship with triangle rendering, movement, rotation, and shooting logic.

shot.py

Defines the player's projectile, handling its drawing and straight-line movement.

asteroid.py

Defines the asteroid entity, including its drawing and recursive .split() logic.

asteroidfield.py

Manages the procedural spawning of new asteroids from the screen edges.

constants.py