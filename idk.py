import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Swing Game")

# Create the player
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2, 50, 50)
player_angle = math.pi / 4  # Initial angle of the rope
rope_length = 100
gravity = 0.5
swing_force = 0.2

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_angle -= swing_force

    # Calculate player position based on angle and rope length
    player.x = WIDTH // 2 - rope_length * math.sin(player_angle)
    player.y = HEIGHT // 2 + rope_length * math.cos(player_angle)

    # Apply gravity to the angle
    player_angle += gravity / rope_length

    # Clear the screen
    screen.fill(BLACK)

    # Draw player and rope
    pygame.draw.line(screen, WHITE, (WIDTH // 2, HEIGHT // 2), (player.x + player.width // 2, player.y + player.height // 2))
    pygame.draw.rect(screen, RED, player)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
