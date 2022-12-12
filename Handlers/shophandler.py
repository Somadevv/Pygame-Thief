import pygame
import Helpers.loadFile
import Helpers.drawText
import Player.inventory
import Player.player
# Load game items
loadFile = Helpers.loadFile.load_file
drawText = Helpers.drawText.DrawText


class Shop:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, surface):
        self.surface = surface
        self.toggleOpen = False
        self.shopItems = loadFile('Data/items.json')
        self.playerInventory = Player.inventory.Inventory(surface)
        self.player = Player.player.Player(surface)

    def open(self):
        self.toggleOpen = True
        self.containerWidth = 750 / 2
        containerHeight = 500 / 2
        self.containerX = (750 / 2) - self.containerWidth / 2
        self.containerY = (500 / 2) - containerHeight / 2
        containerColor = (0, 0, 0)

        pygame.draw.rect(self.surface, containerColor, pygame.Rect(self.containerX, self.containerY,
                                                                   self.containerWidth, containerHeight))
        self.render_items()
        # self.playerInventory.close()

    def render_items(self):
        if pygame.mouse.get_pressed[0] and "buyButton":
            self.buy(self.shopItems[2]["price"], 2)

        for i, item in enumerate(self.shopItems):
            # Grid column spacing
            y_offset = 70
            width = 50
            height = 50
            xPos = (self.containerX + width / 2) + \
                (i % 3) * (self.containerWidth / 3)
            yPos = (self.containerY + height / 2) + y_offset * (i // 3)
            textSize = 14
            textColor = (255, 255, 255)
            if (self.player.gold < self.shopItems[item]["price"]):
                textColor = (230, 50, 8)
            else:
                textColor = (8, 230, 92)
            itemIconWidth = 75
            itemIconHeight = 50
            itemIconX = xPos - itemIconWidth / 2
            itemIconY = yPos - itemIconHeight / 2
            itemLoad = pygame.image.load(
                "Assets/Images/Icons/potion.png").convert_alpha()
            itemImage = pygame.transform.scale(
                itemLoad, (itemIconWidth, itemIconHeight))

            buyButton = pygame.draw.rect(self.surface, (198, 230, 8), pygame.Rect(
                xPos, yPos, width, height), 1)
            renderItemImage = self.surface.blit(
                itemImage, (itemIconX, itemIconY))
            itemPrice = drawText(self.surface, str(self.shopItems[item]["price"]), textSize, textColor,
                                 xPos + width / 2, yPos + height / 2)

    def close(self):
        self.toggleOpen = False

    def buy(self, price, itemId):
        print(itemId)
        self.player.remove_gold(price)
        self.playerInventory.add_item(itemId)

    def sell(self, itemId):
        pass

    def initialize(self):

        if self.toggleOpen:
            self.open()
        else:
            self.close()
