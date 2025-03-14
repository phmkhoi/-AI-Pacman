import pygame
from game_map import TILE_SIDE, OFFSET_HEIGHT, OFFSET_WIDTH, IMAGE_OFFSET

FRAME_DURATION = 30
RADIUS = TILE_SIDE // 2 - 1
HIT_BOX_OFFSET = 5
HIT_BOX_SIZE = 10

class Pacman():
    def __init__(self, x_2DCoord, y_2DCoord, speed, img_list, direction, board):
        self.logic_x = x_2DCoord
        self.logic_y = y_2DCoord
        
        self.display_x, self.display_y = self.turnLogicToDisplay()
        self.speed = speed
        self.img_list = img_list
        self.direction = direction
        self.board = board
        self.hit_box = pygame.Rect(self.display_x + HIT_BOX_OFFSET, self.display_y + HIT_BOX_OFFSET, HIT_BOX_SIZE, HIT_BOX_SIZE)

        self.update_counter = 0
        self.frame_counter = 0
        self.score = 0

    def getPosition(self):
        return self.logic_y, self.logic_x

    def turnLogicToDisplay(self):
        display_x = OFFSET_WIDTH + self.logic_x * TILE_SIDE
        display_y = OFFSET_HEIGHT + self.logic_y * TILE_SIDE

        return display_x, display_y

    def turnDisplayToLogic(self):
        logic_x = (self.display_x - OFFSET_WIDTH) // TILE_SIDE
        logic_y = (self.display_y - OFFSET_HEIGHT) // TILE_SIDE

        return logic_x, logic_y

    def render(self, screen):
        self.update_counter += 1
        if (self.update_counter % 3 == 0):
            if self.frame_counter <= (FRAME_DURATION * (len(self.img_list) - 1) - 1):
                self.frame_counter += 1
            else:
                self.frame_counter = 0

        if self.direction == "RIGHT":
            screen.blit(self.img_list[self.frame_counter // FRAME_DURATION], (self.display_x - IMAGE_OFFSET, self.display_y - IMAGE_OFFSET))
        elif self.direction == "LEFT":
            screen.blit(pygame.transform.flip(self.img_list[self.frame_counter // FRAME_DURATION], True, False), (self.display_x - IMAGE_OFFSET, self.display_y - IMAGE_OFFSET))
        elif self.direction == "UP":
            screen.blit(pygame.transform.rotate(self.img_list[self.frame_counter // FRAME_DURATION], 90), (self.display_x - IMAGE_OFFSET, self.display_y - IMAGE_OFFSET))
        elif self.direction == "DOWN":
            screen.blit(pygame.transform.rotate(self.img_list[self.frame_counter // FRAME_DURATION], 270), (self.display_x - IMAGE_OFFSET, self.display_y - IMAGE_OFFSET))

    def getTurnsAllowed(self, direction_cmd):
        turns_allowed_list = {"RIGHT": False, "LEFT": False, "UP": False, "DOWN": False}
        exact_display_x, exact_display_y = self.turnLogicToDisplay()
        
        if direction_cmd == "RIGHT" or direction_cmd == "LEFT":
            if (self.board[self.logic_y][self.logic_x - 1] < 3):
                turns_allowed_list["LEFT"] = True
            
            if (self.board[self.logic_y][self.logic_x + 1] < 3):
                turns_allowed_list["RIGHT"] = True

            if (exact_display_x == self.display_x and exact_display_y == self.display_y):
                if (self.board[self.logic_y - 1][self.logic_x] < 3):
                    turns_allowed_list["UP"] = True

                if (self.board[self.logic_y + 1][self.logic_x] < 3):
                    turns_allowed_list["DOWN"] = True

        elif direction_cmd == "UP" or direction_cmd == "DOWN":
            if (self.board[self.logic_y - 1][self.logic_x] < 3):
                turns_allowed_list["UP"] = True
            if (self.board[self.logic_y + 1][self.logic_x] < 3):
                turns_allowed_list["DOWN"] = True

            if (exact_display_x == self.display_x and exact_display_y == self.display_y):
                if (self.board[self.logic_y][self.logic_x - 1] < 3):
                    turns_allowed_list["LEFT"] = True

                if (self.board[self.logic_y][self.logic_x + 1] < 3):
                    turns_allowed_list["RIGHT"] = True

        return turns_allowed_list

    def checkCollision(self):
        if self.direction == "LEFT":
            if self.board[self.logic_y][self.logic_x - 1] > 2 and self.display_x == self.logic_x * TILE_SIDE + OFFSET_WIDTH:
                return True
        elif self.direction == "RIGHT":
            if self.board[self.logic_y][self.logic_x + 1] > 2 and self.display_x == self.logic_x * TILE_SIDE + OFFSET_WIDTH:
                return True
        elif self.direction == "UP":
            if self.board[self.logic_y - 1][self.logic_x] > 2 and self.display_y == self.logic_y * TILE_SIDE + OFFSET_HEIGHT:
                return True
        elif self.direction == "DOWN":
            if self.board[self.logic_y + 1][self.logic_x] > 2 and self.display_y == self.logic_y * TILE_SIDE + OFFSET_HEIGHT:
                return True

        return False

    def update(self, direction_cmd, turns_allowed_list):
        self.update_counter += 1

        if self.update_counter % 4 == 0:

            if turns_allowed_list[direction_cmd] == True and ((self.display_x, self.display_y) == (self.logic_x * TILE_SIDE + OFFSET_WIDTH, self.logic_y * TILE_SIDE + OFFSET_HEIGHT)):
                self.direction = direction_cmd

            if not self.checkCollision():
                if self.direction == "RIGHT":
                    self.display_x += self.speed
                if self.direction == "LEFT":
                    self.display_x -= self.speed
                if self.direction == "UP":
                    self.display_y -= self.speed
                if self.direction == "DOWN":
                    self.display_y += self.speed
        
        self.logic_x, self.logic_y = self.turnDisplayToLogic()
        self.hit_box = pygame.Rect(self.display_x + HIT_BOX_OFFSET, self.display_y + HIT_BOX_OFFSET, HIT_BOX_SIZE, HIT_BOX_SIZE)