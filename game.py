import pygame
import World.Levels.test_level as Test_Level
import Player.player as player
import World.world as World
import Controller.controller
import Player.Inventory.inventory

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
playerInstance = player.Player()

# Assign Variables to Imports
worldData = Test_Level.Test_Level()
userControls = Controller.controller.Controller
worldGeneration = World.World
playerInventoryOpen = False
playerInventory = Player.Inventory.inventory.Inventory

# Get Player Inventory on load
playerInventory.GetInventory()


# Player Position on Load
playerInstance.position.x, playerInstance.position.y = worldData.playerStartPosition

# Game loop
while running:
    # Draw World
    worldGeneration.DrawWorld(CANVAS, worldData.rects)
    GAME_WINDOW.blit(CANVAS, (0, 0))

    # Define Delta Time
    dt = CLOCK.tick(GAME_TICK) * .001 * TARGET_FPS

    # Control
    userControls.GameControls(playerInstance)

    # Update Player Position
    playerInstance.update(dt)

    # Draw Background
    CANVAS.fill((255, 255, 255))

    # Draw Player
    playerInstance.draw(CANVAS)

    # Draw Player inventory bag
    playerInventory.DrawInventoryBagToWindow(
        GAME_WINDOW)

    if playerInventoryOpen == True:
        playerInventory.DrawInventory(GAME_WINDOW)
    else:
        playerInventory.CloseInventory(GAME_WINDOW)

    pygame.display.update()
