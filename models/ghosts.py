from game_map import OFFSET_HEIGHT, OFFSET_WIDTH, TILE_SIDE, IMAGE_OFFSET, IMAGE_SCALE, pygame
import random

CAGE_TOP_LEFT_X = 12
CAGE_TOP_LEFT_Y = 14

CAGE_BOTTOM_RIGHT_X = 17
CAGE_BOTTOM_RIGHT_Y = 16

HIT_BOX_OFFSET = 5
HIT_BOX_SIZE = 10

class Ghost:
    def __init__(self, x_2DCoord, y_2DCoord, target, speed, img, status, direction, board, in_cage):
        self.logic_x = x_2DCoord
        self.logic_y = y_2DCoord

        self.display_x, self.display_y = self.turnLogicToDisplay()

        self.target = target
        self.speed = speed
        self.img = img
        self.hit_box = pygame.Rect(self.display_x + HIT_BOX_OFFSET, self.display_y + HIT_BOX_OFFSET, HIT_BOX_SIZE, HIT_BOX_SIZE)
        self.status = status
        self.direction = direction
        self.board = board
        self.update_counter = 0
        self.in_cage = in_cage

    def turnLogicToDisplay(self):
        display_x = OFFSET_WIDTH + self.logic_x * TILE_SIDE
        display_y = OFFSET_HEIGHT + self.logic_y * TILE_SIDE

        return display_x, display_y
    
    def turnDisplayToLogic(self):
        logic_x = (self.display_x - OFFSET_WIDTH) // TILE_SIDE
        logic_y = (self.display_y - OFFSET_HEIGHT) // TILE_SIDE

        return logic_x, logic_y

    def changeStatus(self, status):
        self.status = status

    def getReverseDirection(self):
        reversed_direction = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        self.direction = reversed_direction[self.direction]

    def adjustDirectionNotReverse(self, next_direction):

        if self.direction == self.getReverseDirection():
            vertical_directions = ["UP", "DOWN"]
            horizontal_directions = ["LEFT", "RIGHT"]

            if (next_direction == "UP" or next_direction == "DOWN"):
                return horizontal_directions[random.randint(0, 1)]
            
            if (next_direction == "LEFT" or next_direction == "RIGHT"):
                return vertical_directions[random.randint(0, 1)]
            
        return next_direction

    def checkTurnable(self):
        exact_display_x, exact_display_y = self.turnLogicToDisplay()
        if (exact_display_x != self.display_x or exact_display_y != self.display_y):
            return False

        if self.direction == "LEFT" or self.direction == "RIGHT":
            if (self.board[self.logic_y - 1][self.logic_x] < 3 or self.board[self.logic_y + 1][self.logic_x] < 3):
                return True
        elif self.direction == "UP" or self.direction == "DOWN":
            if (self.board[self.logic_y][self.logic_x - 1] < 3 or self.board[self.logic_y][self.logic_x + 1] < 3):
                return True
            
        return False

    def checkInCage(self):
        if not ((self.logic_x >= CAGE_TOP_LEFT_X and self.logic_x <= CAGE_BOTTOM_RIGHT_X) and (self.logic_y >= CAGE_TOP_LEFT_Y and self.logic_y <= CAGE_BOTTOM_RIGHT_Y)):
            self.in_cage = False

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

    def getDirection(self):
        pass

    def update(self, target):
        
        if self.status == "SCATTER":
            if self.checkTurnable() and self.checkCollision():
                self.direction = self.getDirection()
        elif self.status == "CHASE":
            if self.in_cage:
                self.direction = self.getDirection()
            else:
                if self.checkTurnable():
                    self.direction = self.getDirection()
                

        self.checkInCage()

        self.update_counter += 1
        if self.update_counter % 5 == 0:
            if self.direction == "LEFT":
                self.display_x -= self.speed
            elif self.direction == "RIGHT":
                self.display_x += self.speed
            elif self.direction == "UP":
                self.display_y -= self.speed
            elif self.direction == "DOWN":
                self.display_y += self.speed
            else:
                print("[UNKNOWN DIRECTION]: \"{}\"\n".format(self.direction))

        self.logic_x, self.logic_y = self.turnDisplayToLogic()
        self.target = target
        self.hit_box = pygame.Rect(self.display_x + HIT_BOX_OFFSET, self.display_y + HIT_BOX_OFFSET, HIT_BOX_SIZE, HIT_BOX_SIZE)

    def render(self, screen):
        screen.blit(self.img, (self.display_x - IMAGE_OFFSET, self.display_y - IMAGE_OFFSET))