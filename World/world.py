import pygame


class World():
    def DrawWorld(SURFACE, RECT):
        for i in RECT:
            pygame.draw.rect(SURFACE, (17, 17, 17), i)
