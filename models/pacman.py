import pygame
from game_map import WINDOW_HEIGHT, WINDOW_WIDTH, COLUMN_AMOUNT, ROW_AMOUNT, TILE_SIDE, OFFSET_HEIGHT, OFFSET_WIDTH, BOARD

ANIMATION_FRAME_DURATION = 50
SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

pacman_images = []
for i in range(1, 5):
    pacman_images.append(pygame.transform.scale(pygame.image.load(f'assets/pacman/pacman{i}.png'), (26, 26)))

# #Initialize pacman's position

INIT_PACMAN_X = OFFSET_WIDTH + TILE_SIDE * (COLUMN_AMOUNT // 2 - 1)
INIT_PACMAN_Y = OFFSET_HEIGHT + TILE_SIDE * (ROW_AMOUNT - 9)

PACMAN_RADIUS = TILE_SIDE // 2
PACMAN_SPEED = 1
class Pacman():
    def __init__(self):
        self.x = INIT_PACMAN_X + TILE_SIDE // 2
        self.y = INIT_PACMAN_Y + TILE_SIDE // 2
        #print(INIT_PACMAN_X, INIT_PACMAN_Y, self.x, self.y, end = '\n')

    def draw(self, direction, counter):
        # Define Direction:
        # 0: Right, 1: Left, 2: Up, 3: Down
        if direction == 0:
            SCREEN.blit(pacman_images[counter // ANIMATION_FRAME_DURATION], (self.x, self.y))

        if direction == 1:
            SCREEN.blit(pygame.transform.flip(pacman_images[counter // ANIMATION_FRAME_DURATION], True, False), (self.x, self.y))

        if direction == 2:
            SCREEN.blit(pygame.transform.rotate(pacman_images[counter // ANIMATION_FRAME_DURATION], 90), (self.x, self.y))

        if direction == 3:
            SCREEN.blit(pygame.transform.rotate(pacman_images[counter // ANIMATION_FRAME_DURATION], 270), (self.x, self.y))
    
    def checkPosition(self, direction):
        Turns = [False, False, False, False]
        x = self.x - OFFSET_WIDTH + TILE_SIDE
        y = self.y - OFFSET_HEIGHT + TILE_SIDE

        if (x // COLUMN_AMOUNT < COLUMN_AMOUNT - 1):
            if direction == 0:
                if BOARD[y // TILE_SIDE][(x - PACMAN_RADIUS) // TILE_SIDE] < 3:
                    Turns[1] = True
            if direction == 1:
                if BOARD[y // TILE_SIDE][(x + PACMAN_RADIUS) // TILE_SIDE] < 3:
                    Turns[0] = True
            if direction == 2:
                if BOARD[(y + PACMAN_RADIUS) // TILE_SIDE][x // TILE_SIDE] < 3:
                    Turns[3] = 0
            if direction == 3:
                if BOARD[(y - PACMAN_RADIUS) // TILE_SIDE][x // TILE_SIDE] < 3:
                    Turns[2] = 0

            if direction == 2 or direction == 3:
                if PACMAN_RADIUS - 7 <= x % TILE_SIDE <= PACMAN_RADIUS + 7:
                    if BOARD[(y + PACMAN_RADIUS) // TILE_SIDE][x // TILE_SIDE] < 3:
                        Turns[3] = True
                    if BOARD[(y - PACMAN_RADIUS) // TILE_SIDE][x // TILE_SIDE] < 3:
                        Turns[2] = True
                if PACMAN_RADIUS - 7 <= y % TILE_SIDE <= PACMAN_RADIUS + 7:
                    if BOARD[y // TILE_SIDE][(x - TILE_SIDE) // TILE_SIDE] < 3:
                        Turns[1] = True
                    if BOARD[y // TILE_SIDE][(x + TILE_SIDE) // TILE_SIDE] < 3:
                        Turns[0] = True
            
            if direction == 0 or direction == 1:
                if PACMAN_RADIUS - 7 <= x % TILE_SIDE <= PACMAN_RADIUS + 7:
                    if BOARD[(y + TILE_SIDE) // TILE_SIDE][x // TILE_SIDE] < 3:
                        Turns[3] = True
                    if BOARD[(y - TILE_SIDE) // TILE_SIDE][x // TILE_SIDE] < 3:
                        Turns[2] = True
                if PACMAN_RADIUS - 7 <= y % TILE_SIDE <= PACMAN_RADIUS + 7:
                    if BOARD[y // TILE_SIDE][(x - PACMAN_RADIUS) // TILE_SIDE] < 3:
                        Turns[1] = True
                    if BOARD[y // TILE_SIDE][(x + PACMAN_RADIUS) // TILE_SIDE] < 3:
                        Turns[0] = True
        else:
            Turns[0] = True
            Turns[1] = True

        return Turns

    def collectScores(self, score):
        x = self.x - OFFSET_WIDTH + TILE_SIDE
        y = self.y - OFFSET_HEIGHT + TILE_SIDE
        if 0 < BOARD[y // TILE_SIDE][x // TILE_SIDE] < 3:
            BOARD[y // TILE_SIDE][x // TILE_SIDE] = 0
            score += 1
        
        return score

    def move(self, direction, turn_allowed, direction_changed):
        if direction == 0 and turn_allowed[0] == True:
            self.x += PACMAN_SPEED
        if direction == 1 and turn_allowed[1] == True:
            self.x -= PACMAN_SPEED
        if direction == 2 and turn_allowed[2] == True:
            self.y -= PACMAN_SPEED
        if direction == 3 and turn_allowed[3] == True:
            self.y += PACMAN_SPEED
        
        if self.x > WINDOW_WIDTH:
            self.x = 0  
        elif self.x <= 0:
            self.x = WINDOW_WIDTH - 1

        if direction_changed == True:
            self.x = ((self.x - OFFSET_WIDTH) // TILE_SIDE) * TILE_SIDE + OFFSET_WIDTH + TILE_SIDE // 2
            self.y = ((self.y - OFFSET_HEIGHT) // TILE_SIDE) * TILE_SIDE + OFFSET_HEIGHT + TILE_SIDE // 2