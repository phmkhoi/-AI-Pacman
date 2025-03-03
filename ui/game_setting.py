import pygame

pygame.init()

# Create Window setting
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 950

g_SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
g_TIMER = pygame.time.Clock()
g_FPS = 60