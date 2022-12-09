import pygame
import Helpers.drawText

DrawText = Helpers.drawText.DrawText


class Inventory():
    def __init__(self):
        self.BAG_COLOR = (125, 22, 55)
        self.BAG_HEIGHT = 65
        self.BAG_WIDTH = 65
        self.BAG_XPOS = 20
        self.BAG_YPOS = 350

    def DrawInventoryBagToWindow(self, surface):
        BAG_ICON = pygame.image.load("Assets/Images/Icons/bag.png").convert()
        TEXT_SIZE = 20
        image = pygame.transform.scale(
            BAG_ICON, (self.BAG_WIDTH, self.BAG_HEIGHT))
        surface.blit(image, (self.BAG_XPOS, self.BAG_YPOS))
        DrawText(surface, "Tab", TEXT_SIZE, (255, 255, 255),
                 50, 385)
