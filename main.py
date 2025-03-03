from ui.game_setting import *
from ui.game_map import initUI
from models.pacman import Pacman

#Initialize pacman's position
PACMAN_X = 425
PACMAN_Y = 663

pacmanDirection = 0
animationCounter = 0

#Main game loop
run = True
while run:
    g_TIMER.tick(g_FPS)

    initUI()

    if animationCounter < 19:
        animationCounter += 1
    else:
        animationCounter = 0

    
    pacman = Pacman(PACMAN_X, PACMAN_Y)
    pacman.DrawCharacter(pacmanDirection, animationCounter)

    # Update game state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #-----------------------------------
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         pacmanDirection = 0
        #     elif event.key == pygame.K_LEFT:
        #         pacmanDirection = 1
        #     elif event.key == pygame.K_UP:
        #         pacmanDirection = 2
        #     elif event.key == pygame.K_DOWN:
        #         pacmanDirection = 3
        #-----------------------------------

    pygame.display.flip()

pygame.quit()