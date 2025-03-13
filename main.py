import pygame
from game_map import initUI, WINDOW_HEIGHT, WINDOW_WIDTH
from models.pacman import Pacman

# Functions
def initCharacters():
    # pacman = Pacman()
    pacman = Pacman()
    return pacman
    pass

def renderCharacters(animationCounter, Direction, pacman):
    animationCounter = (animationCounter + 1) % 199
    pacman.draw(Direction, animationCounter)
    return animationCounter
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
pacman_direction_command = 0
pacman_turn_allowed = [False, False, False, False]
animationCounter = 0
move_counter = 0

TIMER.tick(FPS)
pacman = initCharacters()
#Main game loop
while run:
    
    initUI(SCREEN)

    # pacman, ghost_lists = initCharacters()

    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pacman_direction_command = 0
            elif event.key == pygame.K_LEFT:
                pacman_direction_command = 1
            elif event.key == pygame.K_UP:
                pacman_direction_command= 2
            elif event.key == pygame.K_DOWN:
                pacman_direction_command = 3
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and pacman_direction_command == 0:
                pacman_direction_command = pacmanDirection
            elif event.key == pygame.K_LEFT and pacman_direction_command == 1:
                pacman_direction_command = pacmanDirection
            elif event.key == pygame.K_UP and pacman_direction_command == 2:
                pacman_direction_command = pacmanDirection
            elif event.key == pygame.K_DOWN and pacman_direction_command == 3:
                pacman_direction_commandd = pacmanDirection
        
        for i in range(4):
            if pacman_direction_command == i and pacman_turn_allowed[i] == True:
                pacmanDirection = i
    
    #Check Collision
    pacman_turn_allowed = pacman.checkPosition(pacmanDirection)
    #Characters Movement
    if (move_counter == 0):
        pacman.move(pacmanDirection, pacman_turn_allowed)
    move_counter = (move_counter + 1) % 5
    #Change animationCounter and Render Characters
    animationCounter = renderCharacters(animationCounter, pacmanDirection, pacman)
    pygame.display.flip()

pygame.quit()