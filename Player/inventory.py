import pygame
import json
import Helpers.drawText

DrawText = Helpers.drawText.DrawText

# Opening JSON file
test = open('Data/items.json')
data = json.load(test)


class Inventory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, surface):
        self.INVENTORY = {}
        self.toggleInventory = False
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
                DrawText(self.surface, self.INVENTORY[item]["name"], textSize, textColor,
                         xPos + width / 2, yPos + height / 2)

    def open(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.container)
        pygame.draw.rect(self.surface, (255, 255, 255), self.innerContainer)
        self.update()

    def close(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.closeContainer)

    def add_item(self, itemId):

        itemId = str(itemId)
        if itemId in data:
            if itemId not in self.INVENTORY:
                self.INVENTORY[itemId] = {
                    "name": data[itemId]["name"], "price": data[itemId]["price"]}
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
        BAG_HEIGHT = 65
        BAG_WIDTH = 65
        BAG_XPOS = 20
        BAG_YPOS = 350
        BAG_ICON = pygame.image.load("Assets/Images/Icons/bag.png").convert()
        TEXT_SIZE = 20
        image = pygame.transform.scale(
            BAG_ICON, (BAG_WIDTH, BAG_HEIGHT))
        self.surface.blit(image, (BAG_XPOS, BAG_YPOS))
        DrawText(self.surface, "Tab", TEXT_SIZE, (255, 255, 255),
                 50, 385)

    def initialize(self):
        self.draw_bag_to_window()

        if self.toggleInventory:
            self.open()
        else:
            self.close()
