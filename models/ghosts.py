from ui.game_setting import pygame, WINDOW_HEIGHT, WINDOW_WIDTH
from ui.game_map import BOARDS, COLUMN_AMOUNT, ROW_AMOUNT
import ui.game_setting

#Initialize position for each ghost

INIT_BLUE_GHOST_X = 440
INIT_BLUE_GHOST_Y = 388

INIT_PINK_GHOST_X = 440
INIT_PINK_GHOST_Y = 438

INIT_ORANGE_GHOST_X = 440
INIT_ORANGE_GHOST_Y = 438

INIT_RED_GHOST_X = 56
INIT_RED_GHOST_Y = 58

IMAGE_SCALE = 40
HITBOX_MARGIN = 18

class Ghost:
    def __init__(self, xCoord, yCoord, target, speed, img):
        self.x = xCoord
        self.y = yCoord
        self.centerX = xCoord - (IMAGE_SCALE // 2)
        self.centerY = yCoord - (IMAGE_SCALE // 2)

        self.target = target
        self.speed = speed
        self.img = img
        self.path = []
    
    def Draw(self):
        ui.game_setting.g_SCREEN.blit(self.img, (self.x - 5, self.y - 5))

        ghost_border = pygame.rect.Rect(
            (self.centerX - HITBOX_MARGIN, self.centerY - HITBOX_MARGIN), 
            (HITBOX_MARGIN * 2, HITBOX_MARGIN * 2))
        
        return ghost_border

    # def Move(self):
        # if self.path:
        #     nextPos = self.path.pop(0)
        #     self.x, self.y = nextPos
        #     self.centerX = self.x + (IMAGE_SCALE // 2)
        #     self.centerY = self.y + (IMAGE_SCALE // 2)
        #     # self.borderBox = self.Draw()

    # def GetNeighbors(self):
    #     neighbors = []
    #     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    #         newX, newY = self.x + dx, self.y + dy
    #         if (0 <= newX <= COLUMN_AMOUNT - 1) and (0 <= newY <= ROW_AMOUNT - 1) and BOARDS[newY][newX] < 3:
    #             neighbors.append((newX, newY))
        
    #     return neighbors