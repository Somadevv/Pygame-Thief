import pygame
import sys
import Player.Inventory.inventory
import Helpers.drawText


pygame.init()

playerInventory = Player.Inventory.inventory.Inventory()
DrawText = Helpers.drawText.DrawText


# Global variables
CLOCK = pygame.time.Clock()
GAME_TICKRATE = 120
GAME_WIDTH = 750
GAME_HEIGHT = 500
GAME_WINDOW = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

# Game loop
while True:
    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Fill background (BLACK)
    GAME_WINDOW.fill((0, 0, 0))

    # Draw Player inventory bag
    playerInventory.DrawInventoryBagToWindow(
        GAME_WINDOW)

    # Flip the display
    pygame.display.update()
    CLOCK.tick(GAME_TICKRATE)
