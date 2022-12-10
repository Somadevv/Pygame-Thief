import pygame


class Test_Level():
    def __init__(self):
        self.rects = [pygame.rect.Rect(
            0, 415, 750, 30), pygame.rect.Rect(600, 375, 50, 50)]
        self.playerStartPosition = 375, 250
