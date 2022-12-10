import pygame
import World.Levels.test_level as Test_Level
import Player.player as player
import World.world as World
import Controller.controller

# Initialise pygame
pygame.init()

# Draw Screen
SCREEN_WIDTH, SCREEN_HEIGHT = 750, 500
CANVAS = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPS Params
CLOCK = pygame.time.Clock()
TARGET_FPS = 60
GAME_TICK = 120

# Run Game Bool
running = True


# Add Player
Player = player.Player()

# Assign Variables to Imports
worldData = Test_Level.Test_Level()
userControls = Controller.controller.Controller
worldGeneration = World.World


# Player Position on Load
Player.position.x, Player.position.y = worldData.playerStartPosition


# Game loop
while running:

    # Define Delta Time
    dt = CLOCK.tick(GAME_TICK) * .001 * TARGET_FPS

    # Control
    userControls.GameControls(Player)

    # Update Player Position
    Player.update(dt)

    # Draw Background
    CANVAS.fill((255, 255, 255))

    # Draw Player
    Player.draw(CANVAS)

    # Draw World
    worldGeneration.DrawWorld(CANVAS, worldData.rects)
    GAME_WINDOW.blit(CANVAS, (0, 0))
    pygame.display.update()

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
playerInventoryOpen = False

# Get Player Inventory on load
playerInventory.GetInventory(GAME_WINDOW)


# Game loop
while True:
    # Fill background (BLACK)
    GAME_WINDOW.fill((0, 0, 0))

    # Draw Player inventory bag
    playerInventory.DrawInventoryBagToWindow(
        GAME_WINDOW)

    if playerInventoryOpen == True:
        playerInventory.DrawInventory(GAME_WINDOW)
    else:
        playerInventory.CloseInventory(GAME_WINDOW)

    # Binds/Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                playerInventoryOpen = not playerInventoryOpen

    pygame.display.flip()

    # Flip the display
    pygame.display.update()
    CLOCK.tick(GAME_TICKRATE)

