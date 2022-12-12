import pygame
import json
import Helpers.drawText
import Helpers.loadFile

loadFile = Helpers.loadFile.load_file
drawText = Helpers.drawText.DrawText


class Inventory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, surface):
        self.INVENTORY = {}
        self.toggleInventory = False
        self.gameItems = loadFile('Data/items.json')
        self.surface = surface

    def load(self):
        print("Loaded player inventory...")

        self.containerX = 100
        self.containerY = 200
        #  PARENT container
        self.container = pygame.Rect(
            self.containerX, self.containerY, 200, 200)
        #  CHILD container
        self.innerContainer = pygame.Rect(
            self.containerX + 10, self.containerY + 10, 180, 180)
        #  CLOSE
        self.closeContainer = pygame.Rect(
            self.containerX, self.containerY, 0, 0)

    def update(self):
        origin = pygame.Rect(
            150, self.containerY + 20, 20, 20)
        if self.INVENTORY:
            for i, item in enumerate(self.INVENTORY):
                # Grid column spacing
                y_offset = 40
                xPos = 130 + (i % 3) * 80
                yPos = origin.y + y_offset * (i // 3)
                width = 50
                height = 50
                textSize = 15
                textColor = (100, 30, 255)

                pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect(
                    xPos, yPos, width, height), 1)
                drawText(self.surface, self.INVENTORY[item]["name"], textSize, textColor,
                         xPos + width / 2, yPos + height / 2)

    def open(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.container)
        pygame.draw.rect(self.surface, (255, 255, 255), self.innerContainer)
        self.update()

    def close(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.closeContainer)

    def add_item(self, itemId):
        itemId = str(itemId)
        if itemId in self.gameItems:
            if itemId not in self.INVENTORY:
                self.INVENTORY[itemId] = {
                    "name": self.gameItems[itemId]["name"], "price": self.gameItems[itemId]["price"]}
                print("Added", self.INVENTORY)
            else:
                print("Item already in inventory")
        else:
            print("No item with that ID exists")

    def delete_item(self, itemId):
        itemId = str(itemId)

        if itemId not in self.INVENTORY:
            print("No item found with that ID")
        else:
            self.INVENTORY.pop(itemId)

    def pick_up_item(self, item):
        if item in self.INVENTORY:
            print("Duplicate item found")

    def draw_bag_to_window(self):
        bagWidth = 65
        bagHeight = 65
        bagXpos = 20
        bagYpos = 350
        bagIcon = pygame.image.load(
            "Assets/Images/Icons/bag.png").convert_alpha()
        textSize = 20
        image = pygame.transform.scale(
            bagIcon, (bagWidth, bagHeight))
        self.surface.blit(image, (bagXpos, bagYpos))
        drawText(self.surface, "Tab", textSize, (255, 255, 255),
                 50, 385)

    def initialize(self, surface):
        self.draw_bag_to_window()
        self.surface = surface

        if self.toggleInventory:
            self.open()
        else:
            self.close()