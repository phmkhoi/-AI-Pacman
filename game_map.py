import math
import pygame

# use map.py to define elements

# -------- Define colors and pi --------
WALL_COLOR = "blue"
DOT_COLOR = "white"
GATE_COLOR = "white"
PI = math.pi
# --------------------------------------

# ---------- Define map size ----------
COLUMN_AMOUNT = 30
ROW_AMOUNT = 32
TILE_SIDE = 16
# -------------------------------------

# ------- Define window size -------
WINDOW_HEIGHT = 760
WINDOW_WIDTH = 500
OFFSET_HEIGHT = 70
OFFSET_WIDTH = 10
# ----------------------------------
# 32x30 array
BOARD = [
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

def printMap(screen):
    for i in range(len(BOARD)):
        for j in range(len(BOARD[i])):
            if BOARD[i][j] == 1:
                pygame.draw.circle(screen, DOT_COLOR, 
                    (j * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_WIDTH, i * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_HEIGHT), 4)
            
            elif BOARD[i][j] == 2:
                pygame.draw.circle(screen, DOT_COLOR, 
                    (j * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_WIDTH, i * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_HEIGHT), 7)
            
            elif BOARD[i][j] == 3:
                pygame.draw.line(screen, WALL_COLOR, 
                    (j * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_WIDTH, i * TILE_SIDE + OFFSET_HEIGHT), 
                    (j * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_WIDTH, i * TILE_SIDE + TILE_SIDE + OFFSET_HEIGHT))
                
            elif BOARD[i][j] == 4:
                pygame.draw.line(screen, WALL_COLOR,
                    (j * TILE_SIDE + OFFSET_WIDTH, i * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_HEIGHT),
                    (j * TILE_SIDE + TILE_SIDE + OFFSET_WIDTH, i * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_HEIGHT))
                
            elif BOARD[i][j] == 5:
                pygame.draw.arc(screen, WALL_COLOR,
                    [(j * TILE_SIDE + TILE_SIDE * 0.5) + OFFSET_WIDTH, (i * TILE_SIDE + TILE_SIDE * 0.5) + OFFSET_HEIGHT,
                    TILE_SIDE, TILE_SIDE], PI/2, PI, 1)
                
            elif BOARD[i][j] == 6:
                pygame.draw.arc(screen, WALL_COLOR,
                    [(j * TILE_SIDE + TILE_SIDE * 0.5) + OFFSET_WIDTH, (i * TILE_SIDE - TILE_SIDE * 0.5) + OFFSET_HEIGHT,
                    TILE_SIDE, TILE_SIDE], PI, 3 * PI/2, 1)
                
            elif BOARD[i][j] == 7:
                pygame.draw.arc(screen, WALL_COLOR,
                    [(j * TILE_SIDE - TILE_SIDE * 0.5) + OFFSET_WIDTH, (i * TILE_SIDE - TILE_SIDE * 0.5) + OFFSET_HEIGHT,
                    TILE_SIDE, TILE_SIDE], 3 * PI/2, 2 * PI, 1)
                
            elif BOARD[i][j] == 8:
                pygame.draw.arc(screen, WALL_COLOR,
                    [(j * TILE_SIDE - TILE_SIDE * 0.5) + OFFSET_WIDTH, (i * TILE_SIDE + TILE_SIDE * 0.5) + OFFSET_HEIGHT,
                    TILE_SIDE, TILE_SIDE], 0, PI/2, 1)
                
            elif BOARD[i][j] == 9:
                pygame.draw.line(screen, GATE_COLOR,
                    (j * TILE_SIDE + OFFSET_WIDTH, i * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_HEIGHT),
                    (j * TILE_SIDE + TILE_SIDE + OFFSET_WIDTH, i * TILE_SIDE + (0.5 * TILE_SIDE) + OFFSET_HEIGHT))
def initUI(screenscreen):
    screenscreen.fill("black")
    printMap(screenscreen)