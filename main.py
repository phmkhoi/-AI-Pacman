from ui.game_setting import *
from bus.game_logic  import *
from ui.game_map import initUI
from bus.character_factory import InitCharacters

pygame.init()
InitVariables()
InitCharacters()

#Main game loop
while ui.game_setting.run:
    
    initUI()

    HandleEvents()
    DrawCharacter()
    
    pygame.display.flip()

pygame.quit()