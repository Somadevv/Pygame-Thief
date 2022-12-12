import pygame


class Shop:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, surface):
        self.surface = surface
        self.toggleOpen = False

    def open(self):
        self.toggleOpen = True
        containerWidth = 750 / 2
        containerHeight = 500 / 2
        containerX = (750 / 2) - containerWidth / 2
        containerY = (500 / 2) - containerHeight / 2
        containerColor = (0, 0, 0)

        pygame.draw.rect(self.surface, containerColor, pygame.Rect(containerX, containerY,
                                                                   containerWidth, containerHeight))

    def close(self):
        self.toggleOpen = False

    def buy(self, itemId):
        pass

    def sell(self, itemId):
        pass

    def initialize(self):

        if self.toggleOpen:
            self.open()
        else:
            self.close()
