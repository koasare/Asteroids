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