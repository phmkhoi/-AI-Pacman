import pygame
from game_map import initUITestMode, WINDOW_HEIGHT, WINDOW_WIDTH, IMAGE_SCALE, BOARD
from models.blue_ghost import BlueGhost
from models.red_ghost import RedGhost
from models.pink_ghost import PinkGhost
from models.orange_ghost import OrangeGhost
from models.pacman import Pacman


ghost_images_list = []
for i in range (1, 5):
    ghost_images_list.append(pygame.transform.scale(pygame.image.load(f'assets/ghost/ghost{i}.png'), (IMAGE_SCALE, IMAGE_SCALE)))

pacman_frames_list = []
for i in range(1, 5):
    pacman_frames_list.append(pygame.transform.scale(pygame.image.load(f'assets/pacman/pacman{i}.png'), (IMAGE_SCALE, IMAGE_SCALE)))

INIT_GHOST_POS_X = 2
INIT_GHOST_POS_Y = 2

INIT_PACMAN_POS_X = 27
INIT_PACMAN_POS_Y = 30

INIT_GHOST_SPEED = 1

board_map = BOARD
ghost_status = "CHASE"

def initCharacter():
    pacman = Pacman(INIT_PACMAN_POS_X, INIT_PACMAN_POS_Y, 1, pacman_frames_list, "RIGHT", board_map)
    blue_ghost = BlueGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, ghost_images_list[3], ghost_status, "UP", board_map, True)
    red_ghost = RedGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, ghost_images_list[0], ghost_status, "DOWN", board_map, True)
    orange_ghost = OrangeGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, ghost_images_list[1], ghost_status, "UP", board_map, True)
    pink_ghost = PinkGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), 1, ghost_images_list[2], ghost_status, "DOWN", board_map, True)

    ghosts_list = []
    ghosts_list.append(blue_ghost)
    ghosts_list.append(pink_ghost)
    ghosts_list.append(orange_ghost)
    ghosts_list.append(red_ghost)
    return pacman, ghosts_list

def updateGhost(ghost, target):
    ghost.update(target)

def renderOption(screen, title_font, game_font):
    #title = "TEST MODE"
    title_surface = title_font.render(f'TEST MODE', True, (255, 255, 0))
    title_rect = title_surface.get_rect(center = (WINDOW_WIDTH * 3 // 2, WINDOW_HEIGHT // 3))
    screen.blit(title_surface, title_rect)

    option_surface = game_font.render(f'Press one of these keys to choose level', True, (255, 255, 255))
    option_rect = option_surface.get_rect(center = (WINDOW_WIDTH * 3 // 2, WINDOW_HEIGHT // 2))
    screen.blit(option_surface, option_rect)

    level_surface = game_font.render(f'[1] Level 1: Blue ghost using BFS', True, (0, 255, 255))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT * 2 // 3))
    screen.blit(level_surface, level_rect)

    level_surface = game_font.render(f'[2] Level 2: Pink ghost using BFS', True, (255, 153, 255))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT * 2 // 3 + 30))
    screen.blit(level_surface, level_rect)

    level_surface = game_font.render(f'[3] Level 3: Orange ghost using UCS', True, (255, 153, 51))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT * 2 // 3 + 60))
    screen.blit(level_surface, level_rect)

    level_surface = game_font.render(f'[4] Level 4: Red ghost using A*', True, (255, 0, 0))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13// 12), top = (WINDOW_HEIGHT * 2 // 3 + 90))
    screen.blit(level_surface, level_rect)

def renderCharacters(screen, pacman, ghost):
    pacman.render(screen)
    ghost.render(screen)

def renderDuration(screen, game_font, start_time, end_time):
    duration = (end_time - start_time) / 1000
    duration_surface = game_font.render(f'Duration: {duration}s', True, (255, 255, 255))
    duration_rect =  duration_surface.get_rect(left = (WINDOW_WIDTH // 12), top = (WINDOW_HEIGHT * 11 // 12))
    screen.blit(duration_surface, duration_rect)
    
def processOver(ghost, pacman):
    if (pygame.Rect.colliderect(ghost.hit_box, pacman.hit_box)):
        return True
    return False

def testMode():
    SCREEN = pygame.display.set_mode([WINDOW_WIDTH * 2, WINDOW_HEIGHT])

    title_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 30)
    game_font = pygame.font.Font('assets/PressStart2P-vaV7.ttf', 12)

    pacman, ghost_list = initCharacter()

    selected_ghost = 0
    already_selected = False
    process_active = True
    process_over = False
    start_time = 0
    end_time = 0

    run = True
    while run:
        initUITestMode(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if already_selected == False and process_over == False:
                    if event.key == pygame.K_1:
                        selected_ghost = 0
                    elif event.key == pygame.K_2:
                        selected_ghost = 1
                    elif event.key == pygame.K_3:
                        selected_ghost = 2
                    elif event.key == pygame.K_4:
                        selected_ghost = 3

                if event.key == pygame.K_r and process_over == False:
                    start_time = pygame.time.get_ticks()
                    already_selected = True
                    process_active = True

                if event.key == pygame.K_c and process_over == True:
                    pacman, ghost_list = initCharacter()
                    selected_ghost = 0
                    already_selected = False
                    process_over = False
                    process_active = True
        
        if already_selected == True and process_over == False:
            updateGhost(ghost_list[selected_ghost], pacman.getPosition())
        
        process_over = processOver(ghost_list[selected_ghost], pacman)
        if process_over == True:
            if process_active == True:
                end_time = pygame.time.get_ticks()
                process_active = False
            renderDuration(SCREEN, game_font, start_time, end_time)
        renderOption(SCREEN, title_font, game_font)
        renderCharacters(SCREEN, pacman, ghost_list[selected_ghost])
        pygame.display.flip()
    
    pygame.quit()