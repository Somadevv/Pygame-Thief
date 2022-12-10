import pygame
import sys


class Controller():
    def __init__(self):
        self.playerInventoryOpen = False

    def GameControls(self, Player):
        test = pygame.event.get()
        for event in test:
            if event.type == pygame.KEYDOWN:
                # Inventory
                if event.key == pygame.K_TAB:
                    print("opened")
                    self.playerInventoryOpen = not self.playerInventoryOpen
                # Movement
                if event.key == pygame.K_a:
                    Player.LEFT_KEY = True
                elif event.key == pygame.K_d:
                    Player.RIGHT_KEY = True
                elif event.key == pygame.K_SPACE:
                    Player.jump()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    Player.LEFT_KEY = False
                elif event.key == pygame.K_d:
                    Player.RIGHT_KEY = False
                elif event.key == pygame.K_SPACE:
                    Player.velocity.y *= .25
                    Player.is_jumping = False
