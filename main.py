import pygame
from game_map import initUI, WINDOW_HEIGHT, WINDOW_WIDTH
from models.pacman import Pacman

# Functions
def initCharacters():
    # pacman = Pacman()
    pacman = Pacman()
    return pacman
    pass

def renderCharacters(animation_counter, Direction, pacman):
    animation_counter = (animation_counter + 1) % 199
    pacman.draw(Direction, animation_counter)
    return animation_counter
    pass

pygame.init()

# Global Variables
SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
TIMER = pygame.time.Clock()
FPS = 60
ANIMATION_FRAME_DURATION = 50

# Initialize game variables
run = True
pacman_direction = 0
pacman_direction_command = 0
pacman_turn_allowed = [False, False, False, False]
animation_counter = 0
pacman_score = 0
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
                pacman_direction_command = pacman_direction
            elif event.key == pygame.K_LEFT and pacman_direction_command == 1:
                pacman_direction_command = pacman_direction
            elif event.key == pygame.K_UP and pacman_direction_command == 2:
                pacman_direction_command = pacman_direction
            elif event.key == pygame.K_DOWN and pacman_direction_command == 3:
                pacman_direction_commandd = pacman_direction
        
        for i in range(4):
            if pacman_direction_command == i and pacman_turn_allowed[i] == True:
                pacman_direction = i
    
    #Check Collision
    pacman_turn_allowed = pacman.checkPosition(pacman_direction)
    #Characters Movement
    if (move_counter == 0):
        pacman.move(pacman_direction, pacman_turn_allowed)
    move_counter = (move_counter + 1) % 5

    #Collect Score
    pacman_score = pacman.collectScores(pacman_score)
    #Change animationCounter and Render Characters
    animation_counter = renderCharacters(animation_counter, pacman_direction, pacman)
    pygame.display.flip()

print("Total score: ", pacman_score)
pygame.quit()