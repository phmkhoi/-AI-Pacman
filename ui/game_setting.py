import pygame

# Create Window setting
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 760


def InitVariables():
    global run, g_SCREEN, g_TIMER, g_FPS
    global pacmanDirection, animationCounter

    run = True

    g_SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    g_TIMER = pygame.time.Clock()
    g_FPS = 60

    g_TIMER.tick(g_FPS)

    pacmanDirection = 0
    animationCounter = 0