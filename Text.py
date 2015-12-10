import pygame
import pygame.font

def printOnScreen(screen, x, y, text, font, bold = False, italic = False, size = 15, color = (255, 255, 255)):
    text = str(text)
    font = pygame.font.SysFont(font, size, bold, italic)
    text = font.render(text, True, color)
    screen.blit(text, (x,y))