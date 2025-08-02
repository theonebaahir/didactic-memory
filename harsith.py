import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Screen with Rectangle and Text")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font setup
font = pygame.font.SysFont('Arial', 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw a blue rectangle (x, y, width, height)
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))

    # Render text
    text_surface = font.render("Welcome to Pygame!", True, BLACK)
    screen.blit(text_surface, (250, 100))  # Position of the text

    # Update display
    pygame.display.flip()

# Exit Pygame
pygame.quit()
sys.exit()
