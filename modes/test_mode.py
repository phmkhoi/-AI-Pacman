import pygame
from game_map import initUITestMode, WINDOW_HEIGHT, WINDOW_WIDTH, IMAGE_SCALE, BOARD
from models.blue_ghost import BlueGhost
from models.red_ghost import RedGhost
from models.pink_ghost import PinkGhost
from models.orange_ghost import OrangeGhost
from models.pacman import Pacman


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

INIT_GHOST_POS_X = 16
INIT_GHOST_POS_Y = 12

INIT_PACMAN_POS_X = 2
INIT_PACMAN_POS_Y = 2

INIT_GHOST_SPEED = 1

board_map = BOARD
ghost_status = "CHASE"

def initCharacters(board_map):
    pacman = Pacman(INIT_PACMAN_POS_X, INIT_PACMAN_POS_Y, 1, pacman_frames_list, "RIGHT", board_map)
    blue_ghost = BlueGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, blue_ghost_images, ghost_status, "LEFT", board_map, False)
    red_ghost = RedGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, red_ghost_images, ghost_status, "LEFT", board_map, False)
    orange_ghost = OrangeGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, orange_ghost_images, ghost_status, "LEFT", board_map, False)
    pink_ghost = PinkGhost(INIT_GHOST_POS_X, INIT_GHOST_POS_Y, (INIT_PACMAN_POS_Y, INIT_PACMAN_POS_X), INIT_GHOST_SPEED, pink_ghost_images, ghost_status, "LEFT", board_map, False)

    ghosts_list = []
    ghosts_list.append(blue_ghost)
    ghosts_list.append(red_ghost)
    ghosts_list.append(orange_ghost)
    ghosts_list.append(pink_ghost)
    return pacman, ghosts_list

def updateGhost(ghost, target):
    ghost.update(target)

def getPeakMemory(peak_memory, ghost, target):
    memory = ghost.getMemory(target)
    if (peak_memory < memory):
        return memory
    return peak_memory

def getExpandNodes(expand_nodes, ghost, target):
    expand_nodes += ghost.getExpandNodes(target)
    return expand_nodes

def renderOption(screen, title_font, game_font):
    #title = "TEST MODE"
    title_surface = title_font.render(f'TEST MODE', True, (255, 255, 0))
    title_rect = title_surface.get_rect(center = (WINDOW_WIDTH * 3 // 2, WINDOW_HEIGHT // 3))
    screen.blit(title_surface, title_rect)

    option_surface = game_font.render(f'Press one of these keys to choose level', True, (255, 255, 255))
    option_rect = option_surface.get_rect(center = (WINDOW_WIDTH * 3 // 2, WINDOW_HEIGHT * 2 // 3))
    screen.blit(option_surface, option_rect)

    option_surface = game_font.render(f'Press \'C\' to Reset', True, (255, 255, 255))
    option_rect = option_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT // 3 + 30))
    screen.blit(option_surface, option_rect)

    option_surface = game_font.render(f'Press \'R\' to Run', True, (255, 255, 255))
    option_rect = option_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT // 3 + 45))
    screen.blit(option_surface, option_rect)

    option_surface = game_font.render(f'Press \'TAB\' to change character', True, (255, 255, 255))
    option_rect = option_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT // 3 + 60))
    screen.blit(option_surface, option_rect)

    option_surface = game_font.render(f'Press Arrow Keys to move character', True, (255, 255, 255))
    option_rect = option_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT // 3 + 75))
    screen.blit(option_surface, option_rect)

    level_surface = game_font.render(f'[1] Level 1: Blue ghost using BFS', True, (0, 255, 255))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT * 2 // 3 + 20))
    screen.blit(level_surface, level_rect)

    level_surface = game_font.render(f'[2] Level 2: Red ghost using A*', True, (255, 0, 0))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT * 2 // 3 + 50))
    screen.blit(level_surface, level_rect)

    level_surface = game_font.render(f'[3] Level 3: Orange ghost using UCS', True, (255, 153, 51))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT * 2 // 3 + 80))
    screen.blit(level_surface, level_rect)

    level_surface = game_font.render(f'[4] Level 4: Pink ghost using BFS', True, (255, 153, 255))
    level_rect = level_surface.get_rect(left = (WINDOW_WIDTH * 13// 12), top = (WINDOW_HEIGHT * 2 // 3 + 110))
    screen.blit(level_surface, level_rect)

def renderCharacters(screen, pacman, ghost):
    pacman.render(screen)
    ghost.render(screen)

def renderDuration(screen, game_font, start_time, end_time):
    duration = (end_time - start_time) / 1000
    duration_surface = game_font.render(f'Duration: {round(duration , 3)}s', True, (255, 255, 255))
    duration_rect =  duration_surface.get_rect(left = (WINDOW_WIDTH // 12), top = (WINDOW_HEIGHT * 11 // 12) - 25)
    screen.blit(duration_surface, duration_rect)

def renderMemory(screen, game_font, memory):
    memory_kb = memory / 1024
    memory_surface = game_font.render(f'Memory Usage: {round(memory_kb, 3)} KB', True, (255, 255, 255))
    memory_rect =  memory_surface.get_rect(left = (WINDOW_WIDTH // 12), top = (WINDOW_HEIGHT * 11 // 12))
    screen.blit(memory_surface, memory_rect)

def renderExpandNodes(screen, game_font, expand_nodes):
    expand_nodes_surface = game_font.render(f'Expand Nodes: {expand_nodes}', True, (255, 255, 255))
    expand_nodes_rect =  expand_nodes_surface.get_rect(left = (WINDOW_WIDTH // 12), top = (WINDOW_HEIGHT * 11 // 12) + 25)
    screen.blit(expand_nodes_surface, expand_nodes_rect)
    
def processOver(ghost, pacman):
    if (pygame.Rect.colliderect(ghost.hit_box, pacman.hit_box)):
        return True
    return False

def testMode():
    SCREEN = pygame.display.set_mode([WINDOW_WIDTH * 2, WINDOW_HEIGHT])

    title_font = pygame.font.Font('assets/font/PressStart2P-vaV7.ttf', 30)
    game_font = pygame.font.Font('assets/font/PressStart2P-vaV7.ttf', 12)

    pacman, ghost_list = initCharacters(board_map)

    selected_ghost = 0
    already_selected = False
    choosen_character = 0 # 0: Ghost, 1: Pacman
    process_active = True
    process_over = False
    start_time = 0
    end_time = 0
    peak_memory = 0
    expand_nodes = 0

    character_list = [pacman, ghost_list[selected_ghost]]

    run = True
    
    while run:
        initUITestMode(SCREEN, board_map)

        character_string = "Ghost" if choosen_character == 1 else "Pacman"

        character_surface = game_font.render(f'Choosen Character: {character_string}', True, (255, 255, 255))
        character_rect = character_surface.get_rect(left = (WINDOW_WIDTH * 13 // 12), top = (WINDOW_HEIGHT // 3 + 150))
        SCREEN.blit(character_surface, character_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                
                character_list[1] = ghost_list[selected_ghost]

                if already_selected == False and process_over == False:
                    if event.key == pygame.K_1:
                        selected_ghost = 0
                    elif event.key == pygame.K_2:
                        selected_ghost = 1
                    elif event.key == pygame.K_3:
                        selected_ghost = 2
                    elif event.key == pygame.K_4:
                        selected_ghost = 3
                    elif event.key == pygame.K_TAB:
                        choosen_character = choosen_character ^ 1
                    elif event.key == pygame.K_UP:
                        #print("UP")
                        character_list[choosen_character].move("UP")
                    elif event.key == pygame.K_DOWN:
                        #print("DOWN")
                        character_list[choosen_character].move("DOWN")
                    elif event.key == pygame.K_LEFT:
                        #print("LEFT")
                        character_list[choosen_character].move("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        #print("RIGHT")
                        character_list[choosen_character].move("RIGHT")

                if event.key == pygame.K_r and process_over == False:
                    start_time = pygame.time.get_ticks()
                    already_selected = True
                    process_active = True

                if event.key == pygame.K_c and process_over == True:
                    pacman, ghost_list = initCharacters(board_map)
                    selected_ghost = 0
                    already_selected = False
                    process_over = False
                    process_active = True
                    start_time = 0
                    end_time = 0
                    peak_memory = 0
                    expand_nodes = 0
    

        if already_selected == True and process_over == False:
            peak_memory = getPeakMemory(peak_memory, ghost_list[selected_ghost], pacman.getPosition())
            expand_nodes = getExpandNodes(expand_nodes, ghost_list[selected_ghost], pacman.getPosition())
            updateGhost(ghost_list[selected_ghost], pacman.getPosition())
        
        process_over = processOver(ghost_list[selected_ghost], pacman)
        if process_over == True:
            if process_active == True:
                end_time = pygame.time.get_ticks()
                process_active = False
            renderDuration(SCREEN, game_font, start_time, end_time)
            renderMemory(SCREEN, game_font, peak_memory)
            renderExpandNodes(SCREEN, game_font, expand_nodes)
        renderOption(SCREEN, title_font, game_font)
        renderCharacters(SCREEN, pacman, ghost_list[selected_ghost])
        pygame.display.flip()
    
    pygame.quit()