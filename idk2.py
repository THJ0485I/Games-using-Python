import pygame
import sys

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 40
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minecraft-like Game")

# Create a simple grid-based world
world = [[None] * (WIDTH // BLOCK_SIZE) for _ in range(HEIGHT // BLOCK_SIZE)]

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= BLOCK_SIZE
            y //= BLOCK_SIZE
            if world[y][x] is None:
                world[y][x] = GREEN
            else:
                world[y][x] = None

    # Clear the screen
    screen.fill(BLACK)

    # Draw blocks
    for y, row in enumerate(world):
        for x, block in enumerate(row):
            if block is not None:
                pygame.draw.rect(screen, block, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
