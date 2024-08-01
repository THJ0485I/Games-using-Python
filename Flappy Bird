
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -8
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
PIPE_GAP = 150
BIRD_SIZE = 40
PIPE_VELOCITY = 5

# Load bird image
bird_image = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
bird_image.fill(BLUE)


class Bird:
    def __init__(self):
        self.image = bird_image
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += int(self.velocity)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


class Pipe:
    def __init__(self, x):
        self.height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
        self.top_pipe = pygame.Rect(x, 0, PIPE_WIDTH, self.height)
        self.bottom_pipe = pygame.Rect(x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP)

    def move(self):
        self.top_pipe.x -= PIPE_VELOCITY
        self.bottom_pipe.x -= PIPE_VELOCITY

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.top_pipe)
        pygame.draw.rect(screen, (0, 255, 0), self.bottom_pipe)

    def off_screen(self):
        return self.top_pipe.right < 0


def game_loop():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(3)]
    score = 0
    font = pygame.font.Font(None, 36)
    run = True

    while run:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()

        for pipe in pipes:
            pipe.move()
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH))
                score += 1

        for pipe in pipes:
            pipe.draw(win)
            if bird.rect.colliderect(pipe.top_pipe) or bird.rect.colliderect(pipe.bottom_pipe):
                run = False

        bird.draw(win)

        score_text = font.render(f"Score: {score}", True, BLACK)
        win.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    game_loop()


