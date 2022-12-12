from typing import List
import pygame
import Helpers.loadFile
import Helpers.drawText
import Controller.controller
import Player.player
import Player.inventory


loadFile = Helpers.loadFile.load_file
drawText = Helpers.drawText.DrawText

shopItems = loadFile('Data/items.json')

controller = Controller.controller.Controller()


class Button:
    def __init__(self, rect: pygame.Rect) -> None:
        # self.base_rect is going to be the one that never gets modified
        self.base_rect = rect
        # self.rect is going to be the one that is active
        self.rect = rect

    def collidepoint(self, pos: pygame.Vector2) -> bool:
        return self.rect.collidepoint(pos)

    def scale(self, scale_factor=1.2) -> None:
        width = self.base_rect.width * scale_factor
        height = self.base_rect.height * scale_factor

        c_pos = self.base_rect.center

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = c_pos


class Shop:
    # Buy, Sell, Standard/Special Items (tabs?)
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, screen) -> None:
        self.buttons: List[Button()] = []
        self.toggleOpen = False
        self.playerInventory = Player.inventory.Inventory(screen)
        self.player = Player.player.Player(screen)
        self.pressed = False
        self.isCollided = False
        base_pos = pygame.Vector2(750 / 3, 150)

        width = 30
        height = 30
        y_offset = 50
        x_offset = 50

        for i, item in enumerate(shopItems):
            offset_vector = pygame.Vector2(x_offset*(i % 3), y_offset*(i//3))
            pos = base_pos + offset_vector

            rect = pygame.Rect(pos.x, pos.y, width, height)

            self.buttons.append(Button(rect))

    def open(self, screen: pygame.Surface):
        self.containerWidth = screen.get_width() / 2
        self.containerHeight = screen.get_height() / 2
        self.containerX = self.containerWidth - self.containerWidth / 2
        self.containerY = self.containerHeight - self.containerHeight / 2
        self.containerColor = (0, 0, 0)

        pygame.draw.rect(screen, self.containerColor, pygame.Rect(self.containerX, self.containerY,
                                                                  self.containerWidth, self.containerHeight))
        self.draw_buttons(screen)

    def draw_buttons(self, screen: pygame.Surface) -> None:

        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        for i, button in enumerate(self.buttons):
            if button.collidepoint(mouse_pos):
                button.scale(1.2)
                self.player.remove_gold(shopItems[str(i + 1)]["price"])
            else:
                button.scale(1)

            pygame.draw.rect(screen, "white", button.rect)

    def close(self):
        self.toggleOpen = False

    def buy(self, price, itemId):
        print(itemId)
        # self.player.remove_gold(price)
        # self.playerInventory.add_item(itemId)

    def sell(self, itemId):
        pass

    def initialize(self, screen: pygame.Surface):
        if controller.toggleShop:
            self.open(screen)
        else:
            self.close()
