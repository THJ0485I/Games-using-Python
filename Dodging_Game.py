import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodging Game")

# Player properties
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size
player_speed = 7.5

# Enemy properties
enemy_size = 50
enemy_x = random.randint(0, width - enemy_size)
enemy_y = 0
enemy_speed = 40

# Clock
clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Update enemy position
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = 0
        enemy_x = random.randint(0, width - enemy_size)

    # Collision detection
    if (player_x < enemy_x + enemy_size and player_x + player_size > enemy_x and
            player_y < enemy_y + enemy_size and player_y + player_size > enemy_y):
        game_over = True

    # Clear the screen
    screen.fill(black)

    # Draw player and enemy
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()

