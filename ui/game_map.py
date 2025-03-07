import ui.game_setting
from ui.game_setting import pygame, WINDOW_HEIGHT, WINDOW_WIDTH
import math

# use map.py to define elements

WALL_COLOR = "blue"
DOT_COLOR = "white"
GATE_COLOR = "white"
PI = math.pi

COLUMN_AMOUNT = 30
ROW_AMOUNT = 32

# 32x30 array
BOARDS = [
    [5, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 8],
    [3, 5, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 8, 5,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  8, 3],
    [3, 3, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 3, 3,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  3, 3],
    [3, 3, 1, 5,  4, 4, 8, 1,  5, 4, 4, 4,  8, 1, 3, 3,  1, 5, 4, 4,  4, 8, 1, 5,  4, 4, 8, 1,  3, 3],
    [3, 3, 2, 3,  0, 0, 3, 1,  3, 0, 0, 0,  3, 1, 3, 3,  1, 3, 0, 0,  0, 3, 1, 3,  0, 0, 3, 2,  3, 3],
    [3, 3, 1, 6,  4, 4, 7, 1,  6, 4, 4, 4,  7, 1, 6, 7,  1, 6, 4, 4,  4, 7, 1, 6,  4, 4, 7, 1,  3, 3],
    [3, 3, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  3, 3],
    [3, 3, 1, 5,  4, 4, 8, 1,  5, 8, 1, 5,  4, 4, 4, 4,  4, 4, 8, 1,  5, 8, 1, 5,  4, 4, 8, 1,  3, 3],
    [3, 3, 1, 6,  4, 4, 7, 1,  3, 3, 1, 6,  4, 4, 8, 5,  4, 4, 7, 1,  3, 3, 1, 6,  4, 4, 7, 1,  3, 3],
    [3, 3, 1, 1,  1, 1, 1, 1,  3, 3, 1, 1,  1, 1, 3, 3,  1, 1, 1, 1,  3, 3, 1, 1,  1, 1, 1, 1,  3, 3],
    [3, 6, 4, 4,  4, 4, 8, 1,  3, 6, 4, 4,  8, 0, 3, 3,  0, 5, 4, 4,  7, 3, 1, 5,  4, 4, 4, 4,  7, 3],
    [3, 0, 0, 0,  0, 0, 3, 1,  3, 5, 4, 4,  7, 0, 6, 7,  0, 6, 4, 4,  8, 3, 1, 3,  0, 0, 0, 0,  0, 3],
    [3, 0, 0, 0,  0, 0, 3, 1,  3, 3, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  3, 3, 1, 3,  0, 0, 0, 0,  0, 3],
    [7, 0, 0, 0,  0, 0, 3, 1,  3, 3, 0, 5,  4, 4, 9, 9,  4, 4, 8, 0,  3, 3, 1, 3,  0, 0, 0, 0,  0, 6],
    [4, 4, 4, 4,  4, 4, 7, 1,  6, 7, 0, 3,  0, 0, 0, 0,  0, 0, 3, 0,  6, 7, 1, 6,  4, 4, 4, 4,  4, 4],
    [0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 3,  0, 0, 0, 0,  0, 0, 3, 0,  0, 0, 1, 0,  0, 0, 0, 0,  0, 0],
    [4, 4, 4, 4,  4, 4, 8, 1,  5, 8, 0, 3,  0, 0, 0, 0,  0, 0, 3, 0,  5, 8, 1, 5,  4, 4, 4, 4,  4, 4],
    [8, 0, 0, 0,  0, 0, 3, 1,  3, 3, 0, 6,  4, 4, 4, 4,  4, 4, 7, 0,  3, 3, 1, 3,  0, 0, 0, 0,  0, 5],
    [3, 0, 0, 0,  0, 0, 3, 1,  3, 3, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  3, 3, 1, 3,  0, 0, 0, 0,  0, 3],
    [3, 0, 0, 0,  0, 0, 3, 1,  3, 3, 0, 5,  4, 4, 4, 4,  4, 4, 8, 0,  3, 3, 1, 3,  0, 0, 0, 0,  0, 3],
    [3, 5, 4, 4,  4, 4, 7, 1,  6, 7, 0, 6,  4, 4, 8, 5,  4, 4, 7, 0,  6, 7, 1, 6,  4, 4, 4, 4,  8, 3],
    [3, 3, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 3, 3,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  3, 3],
    [3, 3, 1, 5,  4, 4, 8, 1,  5, 4, 4, 4,  8, 1, 3, 3,  1, 5, 4, 4,  4, 8, 1, 5,  4, 4, 8, 1,  3, 3],
    [3, 3, 1, 6,  4, 8, 3, 1,  6, 4, 4, 4,  7, 1, 6, 7,  1, 6, 4, 4,  4, 7, 1, 3,  5, 4, 7, 1,  3, 3],
    [3, 3, 2, 1,  1, 3, 3, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 3,  3, 1, 1, 2,  3, 3],
    [3, 6, 4, 8,  1, 3, 3, 1,  5, 8, 1, 5,  4, 4, 4, 4,  4, 4, 8, 1,  5, 8, 1, 3,  3, 1, 5, 4,  7, 3],
    [3, 5, 4, 7,  1, 6, 7, 1,  3, 3, 1, 6,  4, 4, 8, 5,  4, 4, 7, 1,  3, 3, 1, 6,  7, 1, 6, 4,  8, 3],
    [3, 3, 1, 1,  1, 1, 1, 1,  3, 3, 1, 1,  1, 1, 3, 3,  1, 1, 1, 1,  3, 3, 1, 1,  1, 1, 1, 1,  3, 3],
    [3, 3, 1, 5,  4, 4, 4, 4,  7, 6, 4, 4,  8, 1, 3, 3,  1, 5, 4, 4,  7, 6, 4, 4,  4, 4, 8, 1,  3, 3],
    [3, 3, 1, 6,  4, 4, 4, 4,  4, 4, 4, 4,  7, 1, 6, 7,  1, 6, 4, 4,  4, 4, 4, 4,  4, 4, 7, 1,  3, 3],
    [3, 3, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  3, 3],
    [3, 6, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  7, 3],
    [6, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 4, 4, 4,  4, 7]
]

def printMap():
    TILE_HEIGHT = (WINDOW_HEIGHT // ROW_AMOUNT)
    TILE_WIDTH = (WINDOW_WIDTH // COLUMN_AMOUNT)

    for i in range(len(BOARDS)):
        for j in range(len(BOARDS[i])):
            if BOARDS[i][j] == 1:
                pygame.draw.circle(ui.game_setting.g_SCREEN, DOT_COLOR, 
                    (j * TILE_WIDTH + (0.5 * TILE_WIDTH), i * TILE_HEIGHT + (0.5 * TILE_HEIGHT)), 4)
            
            elif BOARDS[i][j] == 2:
                pygame.draw.circle(ui.game_setting.g_SCREEN, DOT_COLOR, 
                    (j * TILE_WIDTH + (0.5 * TILE_WIDTH), i * TILE_HEIGHT + (0.5 * TILE_HEIGHT)), 10)
            
            elif BOARDS[i][j] == 3:
                pygame.draw.line(ui.game_setting.g_SCREEN, WALL_COLOR, 
                    (j * TILE_WIDTH + (0.5 * TILE_HEIGHT), i * TILE_HEIGHT), 
                    (j * TILE_WIDTH + (0.5 * TILE_HEIGHT), i * TILE_HEIGHT + TILE_HEIGHT))
                
            elif BOARDS[i][j] == 4:
                pygame.draw.line(ui.game_setting.g_SCREEN, WALL_COLOR,
                    (j * TILE_WIDTH, i * TILE_HEIGHT + (0.5 * TILE_HEIGHT)),
                    (j * TILE_WIDTH + TILE_WIDTH, i * TILE_HEIGHT + (0.5 * TILE_HEIGHT)))
                
            elif BOARDS[i][j] == 5:
                pygame.draw.arc(ui.game_setting.g_SCREEN, WALL_COLOR,
                    [(j * TILE_WIDTH + TILE_WIDTH * 0.5), (i * TILE_HEIGHT + TILE_HEIGHT * 0.5),
                    TILE_WIDTH, TILE_HEIGHT], PI/2, PI, 1)
                
            elif BOARDS[i][j] == 6:
                pygame.draw.arc(ui.game_setting.g_SCREEN, WALL_COLOR,
                    [(j * TILE_WIDTH + TILE_WIDTH * 0.5), (i * TILE_HEIGHT - TILE_HEIGHT * 0.5),
                    TILE_WIDTH, TILE_HEIGHT], PI, 3 * PI/2, 1)
                
            elif BOARDS[i][j] == 7:
                pygame.draw.arc(ui.game_setting.g_SCREEN, WALL_COLOR,
                    [(j * TILE_WIDTH - TILE_WIDTH * 0.5), (i * TILE_HEIGHT - TILE_HEIGHT * 0.5),
                    TILE_WIDTH, TILE_HEIGHT], 3 * PI/2, 2 * PI, 1)
                
            elif BOARDS[i][j] == 8:
                pygame.draw.arc(ui.game_setting.g_SCREEN, WALL_COLOR,
                    [(j * TILE_WIDTH - TILE_WIDTH * 0.5), (i * TILE_HEIGHT + TILE_HEIGHT * 0.5),
                    TILE_WIDTH, TILE_HEIGHT], 0, PI/2, 1)
                
            elif BOARDS[i][j] == 9:
                pygame.draw.line(ui.game_setting.g_SCREEN, GATE_COLOR,
                    (j * TILE_WIDTH, i * TILE_HEIGHT + (0.5 * TILE_HEIGHT)),
                    (j * TILE_WIDTH + TILE_WIDTH, i * TILE_HEIGHT + (0.5 * TILE_HEIGHT)))
                
def initUI():
    ui.game_setting.g_SCREEN.fill("black")
    printMap()