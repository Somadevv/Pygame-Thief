import pygame


def DrawText(surface, text, size, color, x, y):
    text = text
    color = color
    x = x
    y = y
    surface = surface
    size = size
    font = pygame.font.Font("freesansbold.ttf", size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    surface.blit(text, textRect)
