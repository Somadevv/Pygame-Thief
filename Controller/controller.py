import pygame
import sys
import game


class Controller():

    def __init__(self):
        self.playerInventoryOpen = False
        self.playerInventory = game.playerInventory

    def GameControls(self, player):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Inventory
                if event.key == pygame.K_TAB:
                    print("opened")
                    self.playerInventoryOpen = not self.playerInventoryOpen
                # Movement
                if event.key == pygame.K_1:
                    self.playerInventory.add_item(1)
                if event.key == pygame.K_2:
                    self.playerInventory.delete_item(1)
                if event.key == pygame.K_a:
                    player.LEFT_KEY = True
                elif event.key == pygame.K_d:
                    player.RIGHT_KEY = True
                elif event.key == pygame.K_SPACE:
                    player.jump()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    playerInventory.update = False
                if event.key == pygame.K_a:
                    player.LEFT_KEY = False
                elif event.key == pygame.K_d:
                    player.RIGHT_KEY = False
                elif event.key == pygame.K_SPACE:
                    player.velocity.y *= .25
                    player.is_jumping = False
