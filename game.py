import pygame
import sys
import Player.Inventory.inventory


pygame.init()

playerInventory = Player.Inventory.inventory.Inventory()


# Global variables
CLOCK = pygame.time.Clock()
GAME_TICKRATE = 120
GAME_WIDTH = 750
GAME_HEIGHT = 500
GAME_WINDOW = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
PlayerInventoryOpen = False

# Get Player Inventory on load
playerInventory.GetInventory()

# Game loop
while True:
    # Fill background (BLACK)
    GAME_WINDOW.fill((0, 0, 0))

    # Draw Player inventory bag
    playerInventory.DrawInventoryBagToWindow(
        GAME_WINDOW)

    if PlayerInventoryOpen == True:
        playerInventory.DrawInventory(GAME_WINDOW)
    else:
        playerInventory.CloseInventory(GAME_WINDOW)

    # Binds/Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                PlayerInventoryOpen = not PlayerInventoryOpen

    pygame.display.flip()

    # Flip the display
    pygame.display.update()
    CLOCK.tick(GAME_TICKRATE)
