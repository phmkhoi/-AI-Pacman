# from game_setting import pygame, WINDOW_HEIGHT, WINDOW_WIDTH, ANIMATION_FRAME_DURATION
# import game_setting
# from ui.game_map import COLUMN_AMOUNT, ROW_AMOUNT

# # Reading animation of Pacman
# pacmanImages = []
# for i in range(1, 5):
#     pacmanImages.append(pygame.transform.scale(pygame.image.load(f'assets/pacman/pacman{i}.png'), (40, 40)))

# #Initialize pacman's position
# INIT_PACMAN_X = (WINDOW_WIDTH // COLUMN_AMOUNT) * (COLUMN_AMOUNT // 2 - 1)
# INIT_PACMAN_Y = (WINDOW_HEIGHT // ROW_AMOUNT) * (ROW_AMOUNT - 9) + 12

# class Pacman():
#     def __init__(self):
#         self.x = INIT_PACMAN_X
#         self.y = INIT_PACMAN_Y

#     def Draw(self, direction, counter):
#         # Define Direction:
#         # 0: Right, 1: Left, 2: Up, 3: Down
#         if direction == 0:
#             game_setting.SCREEN.blit(pacmanImages[counter // ANIMATION_FRAME_DURATION], (self.x, self.y))

#         if direction == 1:
#             game_setting.SCREEN.blit(pygame.transform.flip(pacmanImages[counter // ANIMATION_FRAME_DURATION], True, False), (self.x, self.y))

#         if direction == 2:
#             game_setting.SCREEN.blit(pygame.transform.rotate(pacmanImages[counter // ANIMATION_FRAME_DURATION], 90), (self.x, self.y))

#         if direction == 3:
#             game_setting.SCREEN.blit(pygame.transform.rotate(pacmanImages[counter // ANIMATION_FRAME_DURATION], 270), (self.x, self.y))

    
#     def GetPosition(self):
#         return self.x // (WINDOW_WIDTH // COLUMN_AMOUNT), self.y // (WINDOW_HEIGHT // ROW_AMOUNT)
