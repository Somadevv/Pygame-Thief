import pygame
import sys
import Player.inventory


class Controller():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.toggleShop = False
        # self.shop = Handlers.shopHandler.Shop(self.surface)

    def GameControls(self, player, surface):

        self.playerInventory = Player.inventory.Inventory(surface)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # self.shop.pressed = not self.shop.pressed
                    pass
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print("m_up")
                    # self.shop.pressed = False

            if event.type == pygame.KEYDOWN:
                # Inventory
                if event.key == pygame.K_TAB:
                    self.playerInventory.toggleInventory = not self.playerInventory.toggleInventory
                # Movement
                if event.key == pygame.K_1:
                    self.playerInventory.add_item(1)
                    self.playerInventory.delete_item(2)
                if event.key == pygame.K_g:
                    self.toggleShop = not self.toggleShop
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
                if event.key == pygame.K_a:
                    player.LEFT_KEY = False
                elif event.key == pygame.K_d:
                    player.RIGHT_KEY = False
                elif event.key == pygame.K_SPACE:
                    player.velocity.y *= .25
                    player.is_jumping = False
