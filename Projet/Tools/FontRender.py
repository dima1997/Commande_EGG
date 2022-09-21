import pygame

def RenderFontBold(text, size, colour):
    """Easy function that allows you to render a font quickly"""
    return pygame.font.SysFont("Corbel",size, bold=pygame.font.Font.bold).render(text, True, colour)

def RenderFont(text, size, colour):
    """Easy function that allows you to render a font quickly"""
    return pygame.font.SysFont("Corbel",size).render(text, True, colour)
