import pygame
import json
import Helpers.drawText

DrawText = Helpers.drawText.DrawText

# Opening JSON file
test = open('Data/items.json')
data = json.load(test)


class Inventory():

    def __init__(self, surface):
        self.BAG_COLOR = (125, 22, 55)
        self.BAG_HEIGHT = 65
        self.BAG_WIDTH = 65
        self.BAG_XPOS = 20
        self.BAG_YPOS = 350
        self.INVENTORY = {"1": {"name": "Key", "price": 1000}, "2": {
            "name": "Key", "price": 1000}, "3": {"name": "Key", "price": 1000}}
        self.update = False
        self.isOpen = False
        self.surface = surface
        self.isOpen = False

    def get_inventory(self):
        print("Loading Inventory...")

        self.containerX = 100
        self.containerY = 200
        # Inventory PARENT container
        self.container = pygame.Rect(
            self.containerX, self.containerY, 200, 200)
        # Inventory CHILD container
        self.innerContainer = pygame.Rect(
            self.containerX + 10, self.containerY + 10, 180, 180)
        # Inventory CLOSE
        self.close = pygame.Rect(self.containerX, self.containerY, 0, 0)

    def draw_inventory_bag_to_window(self, surface):
        BAG_ICON = pygame.image.load("Assets/Images/Icons/bag.png").convert()
        TEXT_SIZE = 20
        image = pygame.transform.scale(
            BAG_ICON, (self.BAG_WIDTH, self.BAG_HEIGHT))
        surface.blit(image, (self.BAG_XPOS, self.BAG_YPOS))
        DrawText(surface, "Tab", TEXT_SIZE, (255, 255, 255),
                 50, 385)

    def update_inventory(self, surface):
        print(self.INVENTORY)

        pygame.draw.rect(surface, (0, 0, 0), self.container)
        pygame.draw.rect(surface, (255, 255, 255), self.innerContainer)
        origin = pygame.Rect(
            150, self.containerY + 20, 20, 20)

        y_offset = 40
        for i, item in enumerate(self.INVENTORY):

            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(
                130 + (i % 3) * 40, origin.y + y_offset * (i // 3), 25, 25))

    def close_inventory(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.close)

    def add_item(self, itemId):

        itemId = str(itemId)
        if itemId in data:
            if itemId not in self.INVENTORY:
                print(self.INVENTORY)
                self.INVENTORY[itemId] = {
                    "name": data[itemId]["name"], "price": data[itemId]["price"]}
                print("Added")
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
            print(itemId)
            print(self.INVENTORY)

    def pick_up_item(self, item):
        if item in self.INVENTORY:
            print("Duplicate item found")
