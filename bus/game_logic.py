import ui.game_setting
import bus.character_factory
import pygame
from models.ghosts import Ghost

def DrawCharacter():
    ui.game_setting.animationCounter = (ui.game_setting.animationCounter + 1) % 199

    bus.character_factory.pacman.Draw(ui.game_setting.pacmanDirection, ui.game_setting.animationCounter)

    bus.character_factory.redGhost.Draw()      
        

def HandleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ui.game_setting.run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ui.game_setting.pacmanDirection = 0
            elif event.key == pygame.K_LEFT:
                ui.game_setting.pacmanDirection = 1
            elif event.key == pygame.K_UP:
                ui.game_setting.pacmanDirection = 2
            elif event.key == pygame.K_DOWN:
                ui.game_setting.pacmanDirection = 3

