"""
Reference:

Pacman game: 
https://youtu.be/9H27CimgPsQ?si=q4douzvwSb-77Qpp
https://github.com/plemaster01/PythonPacman.git

Search Algorithms:
Generative AI: Deepseek, ChatGPT, ...
IDS Search: https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/

Timer: https://www.geeksforgeeks.org/pygame-time/
Memory counter (using tracemalloc): https://www.geeksforgeeks.org/monitoring-memory-usage-of-a-running-python-program/
Font: https://www.fontspace.com/press-start-2p-font-f11591

"""

import pygame
import random
from game_map import initUI, WINDOW_HEIGHT, WINDOW_WIDTH, printMap, IMAGE_SCALE, BOARD
from models.blue_ghost import BlueGhost
from models.red_ghost import RedGhost
from models.pink_ghost import PinkGhost
from models.orange_ghost import OrangeGhost
from models.pacman import Pacman
from button import Button
from modes.test_mode import testMode

# ---------- Get Character Images ----------
blue_ghost_images = []
red_ghost_images = []
pink_ghost_images = []
orange_ghost_images = []

for i in range (0, 4):
    blue_ghost_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost/blue({i}).png'), (IMAGE_SCALE, IMAGE_SCALE)))
    red_ghost_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost/red({i}).png'), (IMAGE_SCALE, IMAGE_SCALE)))
    pink_ghost_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost/pink({i}).png'), (IMAGE_SCALE, IMAGE_SCALE)))
    orange_ghost_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost/orange({i}).png'), (IMAGE_SCALE, IMAGE_SCALE)))

pacman_frames_list = []
for i in range(1, 5):
    pacman_frames_list.append(pygame.transform.scale(pygame.image.load(f'assets/pacman/pacman{i}.png'), (IMAGE_SCALE, IMAGE_SCALE)))
# ------------------------------------------

# ------- Characters' position Initialization -------
INIT_BLUE_GHOST_POS_X = 12
INIT_BLUE_GHOST_POS_Y = 16

INIT_RED_GHOST_POS_X = 13
INIT_RED_GHOST_POS_Y = 12

INIT_ORANGE_GHOST_POS_X = 17
INIT_ORANGE_GHOST_POS_Y = 16

INIT_PINK_GHOST_POS_X = 16
INIT_PINK_GHOST_POS_Y = 12

INIT_PACMAN_POS_X = 14
INIT_PACMAN_POS_Y = 24
# ---------------------------------------------------

# ----------------------------- UI Variables -----------------------------
SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
TIMER = pygame.time.Clock()
FPS = 180
ANIMATION_FRAME_DURATION = 50
TIMER.tick(FPS)

SCORE_X = 15
SCORE_Y = 620
# ---------- Game Variables ----------
pacman_direction_command = "RIGHT"
time_counter = 0
game_score = 0
status_time = 0
ghost_status = "CHASE"
score_tiles = {}

SCATTER_TIME_LIMIT = 70
CHASE_TIME_LIMIT = 100

INIT_GHOST_SPEED = 1
REVERSE_DIRECTION = True
GHOSTS_OVERLAPPED = False
HIT_BOX = 1
# -----------------------------------------------

# ------------------------------------------------------------ Functions ------------------------------------------------------------
def initCharacters(board_map):
    pacman = Pacman(INIT_PACMAN_POS_X, INIT_PACMAN_POS_Y, 1, pacman_frames_list, "RIGHT", board_map)
    blue_ghost = BlueGhost(INIT_BLUE_GHOST_POS_X, INIT_BLUE_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, blue_ghost_images, ghost_status, "UP", board_map, True)
    red_ghost = RedGhost(INIT_RED_GHOST_POS_X, INIT_RED_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, red_ghost_images, ghost_status, "LEFT", board_map, True)
    orange_ghost = OrangeGhost(INIT_ORANGE_GHOST_POS_X, INIT_ORANGE_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, orange_ghost_images, ghost_status, "UP", board_map, True)
    pink_ghost = PinkGhost(INIT_PINK_GHOST_POS_X, INIT_PINK_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), 1, pink_ghost_images, ghost_status, "RIGHT", board_map, True)

    ghosts_list = []
    ghosts_list.append(blue_ghost)
    ghosts_list.append(red_ghost)
    ghosts_list.append(orange_ghost)
    ghosts_list.append(pink_ghost)
    return pacman, ghosts_list

def updateGhosts(ghosts_list, target):
    for ghost in ghosts_list:
        ghost.update(target)

def updatePacman(pacman, direction_cmd, turns_allowed_list):
    pacman.update(direction_cmd, turns_allowed_list)

def renderCharacters(pacman, ghosts_list):
    pacman.render(SCREEN)
    for ghost in ghosts_list:
        ghost.render(SCREEN)

def checkGameOver(ghosts_list, pacman):
    for ghost in ghosts_list:
        # if (ghost.logic_x == pacman.logic_x) and (ghost.logic_y == pacman.logic_y):
        # if (ghost.hit_box.colliderect(pacman.hit_box)):
        if (pygame.Rect.colliderect(ghost.hit_box, pacman.hit_box)):
            return True
    return False

def getScore(pacman, board_map):
    global game_score

    if (board_map[pacman.logic_y][pacman.logic_x] == 1):
        board_map[pacman.logic_y][pacman.logic_x] = 0
        game_score += 1
        score_tiles[(pacman.logic_y, pacman.logic_x)] = 1

    elif (board_map[pacman.logic_y][pacman.logic_x] == 2):
        board_map[pacman.logic_y][pacman.logic_x] = 0
        game_score += 10
        score_tiles[(pacman.logic_y, pacman.logic_x)] = 2

def setGhostsStatus(ghosts_list, status):
    for ghost in ghosts_list:
        ghost.changeStatus(status)

def changeGhostStatus(ghosts_list):
    global status_time, ghost_status

    if ghost_status == "SCATTER":
        ghost_status = "CHASE"
        status_time = random.randint(CHASE_TIME_LIMIT - 10, CHASE_TIME_LIMIT)
        setGhostsStatus(ghosts_list, "CHASE")
    elif ghost_status == "CHASE":
        ghost_status = "SCATTER"
        status_time = random.randint(SCATTER_TIME_LIMIT - 10, SCATTER_TIME_LIMIT)
        setGhostsStatus(ghosts_list, "SCATTER")

def checkGhostsCollision(ghost, other_ghost):
    if (ghost.hit_box.colliderect(other_ghost.hit_box)):
        return True

    return False

pygame.init()

def makeGhostOverlapped(ghosts_list, bool):
    if bool == False:
        for i in range(0, len(ghosts_list) - 1):
            for j in range(i + 1, len(ghosts_list)):
                if (checkGhostsCollision(ghosts_list[i], ghosts_list[j])):
                    ghosts_list[i].getReverseDirection()
                    ghosts_list[j].getReverseDirection()

def renderScore(screen, score):
    font = pygame.font.Font("assets/font/PressStart2P-vaV7.ttf", 14)
    text = font.render(f"Score = {score}", True, (255, 255, 255))
    screen.blit(text, (SCORE_X, SCORE_Y))

def renderStatusTimer(ghosts_list):
    global time_counter, status_time, ghost_status

    time_counter += 1
    if time_counter % 60 == 0:
        if (status_time == 0):
            changeGhostStatus(ghosts_list)
        else:
            status_time -= 1

    font = pygame.font.Font("assets/font/PressStart2P-vaV7.ttf", 14)
    if (ghost_status == "CHASE"):
        text = font.render(f"Chase Time: {status_time}", True, (255, 255, 255))
    elif (ghost_status == "SCATTER"):
        text = font.render(f"Scatter Time: {status_time}", True, (255, 255, 255))
    SCREEN.blit(text, (15, 640))

def initMap(board):
    if len(score_tiles) > 0:
        for tile in score_tiles:
            score = score_tiles[tile]
            board[tile[0]][tile[1]] = score
    score_tiles.clear()

# -----------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------ SCREEN ------------------------------------------------
def main_menu():
    pygame.event.clear()
    pygame.display.set_caption("MENU")
    button_choice = 0

    arrow_button = Button(pos = (50, 400 + button_choice * 60), img = pygame.image.load(f'assets/button/arrow.png'))
    game_mode_button = Button(pos = (100, 400), img = pygame.image.load(f'assets/button/game_mode.png'))
    test_mode_button = Button(pos = (100, 460), img = pygame.image.load(f'assets/button/test_mode.png'))
    exit_button = Button(pos = (172, 520), img = pygame.image.load(f'assets/button/exit.png'))

    while True:
        SCREEN.fill("black")
        SCREEN.blit(pygame.transform.scale(pygame.image.load(f'assets/title.png'), (470, 200)), (13, 70))

        for button in [game_mode_button, test_mode_button, exit_button, arrow_button]:
            button.render(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    button_choice -= 1
                elif event.key == pygame.K_DOWN:
                    button_choice += 1
                elif event.key == pygame.K_RETURN:
                    if button_choice == 0:
                        game_mode()
                    elif button_choice == 1:
                        testMode()
                    elif button_choice == 2:
                        pygame.quit()

            if button_choice < 0:
                    button_choice = 2
            elif button_choice > 2:
                button_choice = 0

        arrow_button.update((50, 400 + button_choice * 60))
        pygame.display.update()

def game_over_screen():
    global game_score

    game_score = 0

    SCREEN.fill("black")
    
    font = pygame.font.Font("assets/font/Emulogic-zrEw.ttf", 50)
    text = font.render("GAME OVER", True, "#b1a04d")
    SCREEN.blit(text, (20, 300))
    pygame.display.update()
    pygame.time.wait(3000)

def game_mode():
    board_map = BOARD
    pacman, ghosts_list = initCharacters(board_map)

    pygame.event.clear()
    pygame.display.set_caption("GAME MODE")
    global pacman_direction_command
    game_run = True  
    waiting_for_key = True

    initMap(board_map)

    while game_run:

        initUI(SCREEN)
        printMap(SCREEN, board_map)      
        renderCharacters(pacman, ghosts_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                
            if waiting_for_key and event.type == pygame.KEYDOWN:
                waiting_for_key = False

        if not waiting_for_key:
            renderCharacters(pacman, ghosts_list)
            renderStatusTimer(ghosts_list)
            renderScore(SCREEN, game_score)

            pressed_key = pygame.key.get_pressed()

            if pressed_key[pygame.K_RIGHT]:
                pacman_direction_command = "RIGHT"
            elif pressed_key[pygame.K_LEFT]:
                pacman_direction_command = "LEFT"
            elif pressed_key[pygame.K_UP]:
                pacman_direction_command = "UP"
            elif pressed_key[pygame.K_DOWN]:
                pacman_direction_command = "DOWN"
            elif pressed_key[pygame.K_ESCAPE]:
                game_run = False
                pygame.time.wait(1500)
                game_over_screen()
                main_menu()

            pacman_turns_allowed_list = pacman.getTurnsAllowed(pacman_direction_command)

            makeGhostOverlapped(ghosts_list, False)  

            updateGhosts(ghosts_list, pacman.getPosition())
            updatePacman(pacman, pacman_direction_command, pacman_turns_allowed_list)
            getScore(pacman, board_map)

            if (checkGameOver(ghosts_list, pacman)):
                game_run = False
                pygame.time.wait(1500)
                game_over_screen()
                main_menu()
        else:
            font = pygame.font.Font("assets/font/PressStart2P-vaV7.ttf", 14)
            text = font.render("Press any key to start", True, (255, 255, 255))
            SCREEN.blit(text, (15, 620))
        pygame.display.update()

    pygame.quit()

# --------------------------------------------------------------------------------------------------------



# -------------------------------------------- MAIN --------------------------------------------
main_menu()