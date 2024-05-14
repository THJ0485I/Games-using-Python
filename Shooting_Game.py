import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Create the player
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 50, 50, 50)

# Create enemies list
enemies = []

# Create bullets list
bullets = []

# Set up the game clock
clock = pygame.time.Clock()

# Count the number of enemies
numberofEnemies = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - 2, player.top, 4, 10)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 7.5
    if keys[pygame.K_RIGHT]:
        player.x += 7.5

    # Update bullets
    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    # Create enemies
    if random.randint(0, 500) < 2:
        enemy = pygame.Rect(random.randint(0, WIDTH - 40), 0, 40, 40)
        enemies.append(enemy)
        numberofEnemies += 1
        if numberofEnemies > 6:
            enemies.remove(enemy)
            numberofEnemies = 0

    # Update enemies
    for enemy in enemies:
        enemy.y += 1  # SPEED
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    if player.y > WIDTH:
        player.y = player.y


    # Check for collisions
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Clear the screen
    screen.fill(BLACK)

    # Draw player, enemies, and bullets
    pygame.draw.rect(screen, GREEN, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
