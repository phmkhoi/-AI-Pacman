from models.pacman import Pacman
from models.red_ghost import RedGhost
from ui.game_setting import WINDOW_HEIGHT, WINDOW_WIDTH
from ui.game_map import COLUMN_AMOUNT, ROW_AMOUNT
import pygame

img = pygame.transform.scale(pygame.image.load(f'assets/ghost/ghost1.png'), (40, 40))

def InitCharacters():
    global pacman, redGhost
    pacman = Pacman()

    redGhost = RedGhost((WINDOW_WIDTH // COLUMN_AMOUNT) * 2, (WINDOW_HEIGHT // ROW_AMOUNT) * 2, (15, 15), 0.5, img)