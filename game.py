import pygame
import sys
import World.Levels.test_level as Test_Level
import Player.player as player
import World.world as World
import Controller.controller
import Player.inventory
import Handlers.shopHandler

# Initialise pygame
pygame.init()

# Draw Screen
SCREEN_WIDTH, SCREEN_HEIGHT = 750, 500
CANVAS = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPS Params
CLOCK = pygame.time.Clock()
TARGET_FPS = 1
GAME_TICK = 120

# Run Game Bool
running = True


# Add Player
playerInstance = player.Player(GAME_WINDOW)

# Assign Variables to Imports
worldData = Test_Level.Test_Level()
userControls = Controller.controller.Controller()
worldGeneration = World.World
inventory = Player.inventory.Inventory(GAME_WINDOW)
shopHandler = Handlers.shopHandler.Shop()

# Get Player Inventory on load
inventory.load()


# Player Position on Load
playerInstance.position.x, playerInstance.position.y = worldData.playerStartPosition
3
# Game loop
while running:
    # Draw World
    worldGeneration.DrawWorld(CANVAS, worldData.rects)
    GAME_WINDOW.blit(CANVAS, (0, 0))

    # Define Delta Time
    dt = CLOCK.tick(GAME_TICK) * .001 * TARGET_FPS

    # Control
    userControls.GameControls(playerInstance, CANVAS)

    # Update Player Position
    playerInstance.initialize(dt)

    # Draw Background
    CANVAS.fill((77, 77, 77))

    # Draw Player
    playerInstance.draw(GAME_WINDOW)

    # Draw Player inventory
    inventory.initialize(GAME_WINDOW)

    # Draw Player inventory
    shopHandler.initialize(GAME_WINDOW)

    pygame.display.update()
