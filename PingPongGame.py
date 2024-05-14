# install pygame

import pygame
import sys

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
BALL_SPEED = [5, 5]
PADDLE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Create the paddles and ball
player_paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 20, 100, 10)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        player_paddle.x += PADDLE_SPEED

    # Move the ball
    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        BALL_SPEED[0] = -BALL_SPEED[0]
    if ball.top <= 0 or ball.colliderect(player_paddle):
        BALL_SPEED[1] = -BALL_SPEED[1]

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
