import pygame
import random
from game_map import initUI, WINDOW_HEIGHT, WINDOW_WIDTH, BOARD, TILE_SIDE, OFFSET_HEIGHT, OFFSET_WIDTH, IMAGE_SCALE
from models.blue_ghost import BlueGhost
from models.red_ghost import RedGhost
from models.pink_ghost import PinkGhost
from models.orange_ghost import OrangeGhost
from models.pacman import Pacman

# ---------- Get Character Images ----------
ghost_images_list = []
for i in range (1, 5):
    ghost_images_list.append(pygame.transform.scale(pygame.image.load(f'assets/ghost/ghost{i}.png'), (IMAGE_SCALE, IMAGE_SCALE)))

pacman_frames_list = []
for i in range(1, 5):
    pacman_frames_list.append(pygame.transform.scale(pygame.image.load(f'assets/pacman/pacman{i}.png'), (IMAGE_SCALE, IMAGE_SCALE)))
# ------------------------------------------

# ------- Characters' position Initialization -------
INIT_BLUE_GHOST_POS_X = 12
INIT_BLUE_GHOST_POS_Y = 16

INIT_RED_GHOST_POS_X = 14
INIT_RED_GHOST_POS_Y = 15

INIT_ORANGE_GHOST_POS_X = 15
INIT_ORANGE_GHOST_POS_Y = 16

# 14 14
INIT_PINK_GHOST_POS_X = 15
INIT_PINK_GHOST_POS_Y = 12

INIT_PACMAN_POS_X = 14
INIT_PACMAN_POS_Y = 24
# ---------------------------------------------------

# ---------- Game Variables ----------
SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
TIMER = pygame.time.Clock()
FPS = 180
ANIMATION_FRAME_DURATION = 50
TIMER.tick(FPS)

board_map = BOARD
run = True
pacman_direction_command = "RIGHT"
time_counter = 0
game_score = 0
status_time = 0
ghost_status = "SCATTER"

SCATTER_TIME_LIMIT = 170
CHASE_TIME_LIMIT = 150

INIT_GHOST_SPEED = 1
REVERSE_DIRECTION = True
GHOSTS_OVERLAPPED = False
HIT_BOX = 3
# -----------------------------------------------

# ------------------------------------------------------------ Functions ------------------------------------------------------------
def initCharacters():
    pacman = Pacman(INIT_PACMAN_POS_X, INIT_PACMAN_POS_Y, 1, pacman_frames_list, "RIGHT", board_map)
    blue_ghost = BlueGhost(INIT_BLUE_GHOST_POS_X, INIT_BLUE_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, ghost_images_list[3], ghost_status, "UP", board_map, True)
    red_ghost = RedGhost(INIT_RED_GHOST_POS_X, INIT_RED_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, ghost_images_list[0], ghost_status, "DOWN", board_map, True)
    orange_ghost = OrangeGhost(INIT_ORANGE_GHOST_POS_X, INIT_ORANGE_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, ghost_images_list[1], ghost_status, "UP", board_map, True)
    # pink_ghost = PinkGhost(INIT_PINK_GHOST_POS_X, INIT_PINK_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), 1, ghost_images_list[2], ghost_status, "DOWN", board_map, True)

    ghosts_list = []
    ghosts_list.append(blue_ghost)
    ghosts_list.append(red_ghost)
    ghosts_list.append(orange_ghost)
    # ghosts_list.append(pink_ghost)
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

def pauseGame():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Press 'P' to unpause
                    paused = False

        # Display a "Paused" message (optional)
        font = pygame.font.SysFont("comicsansms", 14)
        text = font.render("Paused. Press P to resume.", True, (255, 255, 255))
        SCREEN.blit(text, (15, 600))
        pygame.display.update()

        # # Limit the frame rate while paused
        # TIMER.tick(15)

def gameOver(ghosts_list, pacman):
    for ghost in ghosts_list:
        # if (ghost.logic_x == pacman.logic_x) and (ghost.logic_y == pacman.logic_y):
        # if (ghost.hit_box.colliderect(pacman.hit_box)):
        if (pygame.Rect.colliderect(ghost.hit_box, pacman.hit_box)):
            return True
    return False

def getScore(pacman):
    global game_score

    if (board_map[pacman.logic_y][pacman.logic_x] == 1):
        board_map[pacman.logic_y][pacman.logic_x] = 0
        game_score += 1
    elif (board_map[pacman.logic_y][pacman.logic_x] == 2):
        board_map[pacman.logic_y][pacman.logic_x] = 0
        game_score += 10

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
pacman, ghosts_list = initCharacters()

def makeGhostOverlapped(bool):
    if bool == False:
        for i in range(0, len(ghosts_list) - 1):
            for j in range(i + 1, len(ghosts_list)):
                if (checkGhostsCollision(ghosts_list[i], ghosts_list[j])):
                    ghosts_list[i].getReverseDirection()
                    ghosts_list[j].getReverseDirection()

def renderStatusTimer():
    global time_counter, status_time, ghost_status, ghosts_list

    time_counter += 1
    if time_counter % 60 == 0:
        if (status_time == 0):
            changeGhostStatus(ghosts_list)
        else:
            status_time -= 1

    font = pygame.font.SysFont("comicsansms", 14)
    if (ghost_status == "CHASE"):
        text = font.render(f"CHASE: {status_time}", True, (255, 255, 255))
    elif (ghost_status == "SCATTER"):
        text = font.render(f"SCATTER: {status_time}", True, (255, 255, 255))
    SCREEN.blit(text, (15, 630))

# -----------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------- Main game loop ---------------------------------------------------------
while run:
    initUI(SCREEN, game_score)
    renderStatusTimer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pacman_direction_command = "RIGHT"
            elif event.key == pygame.K_LEFT:
                pacman_direction_command = "LEFT"
            elif event.key == pygame.K_UP:
                pacman_direction_command = "UP"
            elif event.key == pygame.K_DOWN:
                pacman_direction_command = "DOWN"

    pacman_turns_allowed_list = pacman.getTurnsAllowed(pacman_direction_command)

    makeGhostOverlapped(False)  

    updateGhosts(ghosts_list, pacman.getPosition())
    updatePacman(pacman, pacman_direction_command, pacman_turns_allowed_list)
    getScore(pacman)


    renderCharacters(pacman, ghosts_list)

    if (gameOver(ghosts_list, pacman)):
        pauseGame()
        run = False

    pygame.display.flip()

pygame.quit()