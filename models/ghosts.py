# from game_setting import pygame, WINDOW_HEIGHT, WINDOW_WIDTH
# from ui.game_map import BOARDS, COLUMN_AMOUNT, ROW_AMOUNT
# import game_setting

# #Initialize position for each ghost

# INIT_BLUE_GHOST_X = 440
# INIT_BLUE_GHOST_Y = 388

# INIT_PINK_GHOST_X = 440
# INIT_PINK_GHOST_Y = 438

# INIT_ORANGE_GHOST_X = 440
# INIT_ORANGE_GHOST_Y = 438

# INIT_RED_GHOST_X = (WINDOW_WIDTH // COLUMN_AMOUNT) * 2
# INIT_RED_GHOST_Y = (WINDOW_HEIGHT // ROW_AMOUNT) * 2

# HITBOX_MARGIN = 18

# class Ghost:
#     def __init__(self, xCoord, yCoord, target, speed, img):
#         self.x = xCoord
#         self.y = yCoord

#         # self.displayX;
#         # self.displayY;

#         self.target = target
#         self.speed = speed
#         self.img = img
#         # self.direction

#     def CheckTurnable(self, BOARDS):
#         pass

#     def Draw(self):
#         game_setting.SCREEN.blit(self.img, ((WINDOW_WIDTH // COLUMN_AMOUNT) * self.x - 5, (WINDOW_HEIGHT // ROW_AMOUNT) * self.y - 5))

#     def FindPath(self):
#         pass

#     def Move(self):
#         if self.path:
#             nextPos = self.path.pop()
#             self.y, self.x = nextPos

#     def Update(self):
#         self.Draw()
#         self.FindPath()
#         self.Move()