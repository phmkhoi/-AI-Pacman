import pygame
from game_map import initUI, WINDOW_HEIGHT, WINDOW_WIDTH

# Functions
def initCharacters():
    # pacman = Pacman()
    pass

def renderCharacters():
    pass

pygame.init()

# Global Variables
SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
TIMER = pygame.time.Clock()
FPS = 60
ANIMATION_FRAME_DURATION = 50

# Initialize game variables
run = True
pacmanDirection = 0
animationCounter = 0

TIMER.tick(FPS)

#Main game loop
while run:
    
    initUI(SCREEN)

    # pacman, ghost_lists = initCharacters()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         pacmanDirection = 0
        #     elif event.key == pygame.K_LEFT:
        #         pacmanDirection = 1
        #     elif event.key == pygame.K_UP:
        #         pacmanDirection = 2
        #     elif event.key == pygame.K_DOWN:
        #         pacmanDirection = 3

    pygame.display.flip()

pygame.quit()