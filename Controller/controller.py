import pygame
import sys
import Player.Inventory.inventory


class Controller():

    def __init__(self, surface):
        self.playerInventoryOpen = False
        self.playerInventory = Player.Inventory.inventory.Inventory(surface)

    def GameControls(self, player):
        test = pygame.event.get()
        for event in test:
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
                    self.playerInventory.update = False
                if event.key == pygame.K_a:
                    player.LEFT_KEY = False
                elif event.key == pygame.K_d:
                    player.RIGHT_KEY = False
                elif event.key == pygame.K_SPACE:
                    player.velocity.y *= .25
                    player.is_jumping = False
