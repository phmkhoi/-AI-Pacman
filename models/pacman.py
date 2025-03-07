from ui.game_setting import pygame, WINDOW_HEIGHT, WINDOW_WIDTH
import ui.game_setting
from ui.game_map import COLUMN_AMOUNT, ROW_AMOUNT

ANIMATION_FRAME_DURATION = 50

# Reading animation of Pacman
pacmanImages = []
for i in range(1, 5):
    pacmanImages.append(pygame.transform.scale(pygame.image.load(f'assets/pacman/pacman{i}.png'), (40, 40)))

#Initialize pacman's position
INIT_PACMAN_X = (WINDOW_WIDTH // COLUMN_AMOUNT) * (COLUMN_AMOUNT // 2 - 1)
INIT_PACMAN_Y = (WINDOW_HEIGHT // ROW_AMOUNT) * (ROW_AMOUNT - 9)

class Pacman():
    def __init__(self):
        self.x = INIT_PACMAN_X
        self.y = INIT_PACMAN_Y
        self.centerX = (INIT_PACMAN_X + (WINDOW_WIDTH // COLUMN_AMOUNT) / 2)
        self.centerY = (INIT_PACMAN_Y + (WINDOW_HEIGHT // ROW_AMOUNT) / 2)

    def Draw(self, direction, counter):
        # Define Direction:
        # 0: Right, 1: Left, 2: Up, 3: Down
        if direction == 0:
            ui.game_setting.g_SCREEN.blit(pacmanImages[counter // ANIMATION_FRAME_DURATION], (self.centerX, self.centerY))

        if direction == 1:
            ui.game_setting.g_SCREEN.blit(pygame.transform.flip(pacmanImages[counter // ANIMATION_FRAME_DURATION], True, False), (self.centerX, self.centerY))

        if direction == 2:
            ui.game_setting.g_SCREEN.blit(pygame.transform.rotate(pacmanImages[counter // ANIMATION_FRAME_DURATION], 90), (self.centerX, self.centerY))

        if direction == 3:
            ui.game_setting.g_SCREEN.blit(pygame.transform.rotate(pacmanImages[counter // ANIMATION_FRAME_DURATION], 270), (self.centerX, self.centerY))
