from ui.game_setting import g_SCREEN, pygame

ANIMATION_FRAME_DURATION = 5

# Reading animation of Pacman
pacmanImages = []
for i in range(1, 5):
    pacmanImages.append(pygame.transform.scale(pygame.image.load(f'assets/pacman/pacman{i}.png'), (45, 45)))

class Pacman():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def DrawCharacter(self, direction, counter):
        # Define Direction:
        # 0: Right, 1: Left, 2: Up, 3: Down
        if direction == 0:
            g_SCREEN.blit(pacmanImages[counter // ANIMATION_FRAME_DURATION], (self.x, self.y))

        if direction == 1:
            g_SCREEN.blit(pygame.transform.flip(pacmanImages[counter // ANIMATION_FRAME_DURATION], True, False), (self.x, self.y))

        if direction == 2:
            g_SCREEN.blit(pygame.transform.rotate(pacmanImages[counter // ANIMATION_FRAME_DURATION], 90), (self.x, self.y))

        if direction == 3:
            g_SCREEN.blit(pygame.transform.rotate(pacmanImages[counter // ANIMATION_FRAME_DURATION], 270), (self.x, self.y))
