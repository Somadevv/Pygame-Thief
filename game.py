import pygame, sys
pygame.init()

# Global variables
CLOCK = pygame.time.Clock()
GAME_TICKRATE = 120
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500

# Colors
COLOR_WHITE = 255, 255, 255

GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
while True:
    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()

    # Fill the background with white
    GAME_WINDOW.fill((COLOR_WHITE))

    # Draw a solid blue circle in the center
    pygame.draw.circle(GAME_WINDOW, (0, 0, 255), (250, 250), 75)

    #This is from harry

    # Flip the display
    pygame.display.update()
    CLOCK.tick(GAME_TICKRATE)

