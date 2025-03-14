from models.ghosts import Ghost, IMAGE_OFFSET, IMAGE_SCALE
from algorithms import DFSSearch, getRandomMove, reconstructPath

class PinkGhost(Ghost):
    def __init__(self, x_2DCoord, y_2DCoord, target, speed, img, status, direction, board, in_cage):
        super().__init__(x_2DCoord, y_2DCoord, target, speed, img, status, direction, board, in_cage)

    def getDirection(self):
        if self.status == "CHASE":
            tracer = DFSSearch(self.board, (self.logic_y, self.logic_x), self.target)
            path = reconstructPath(tracer, (self.logic_y, self.logic_x), self.target)

            next_tile = path[0]
            
        elif self.status == "SCATTER":
            next_tile = getRandomMove(self.board, (self.logic_y, self.logic_x))

        if next_tile[0] > self.logic_y:
            return self.adjustDirectionNotReverse("DOWN")
        elif next_tile[0] < self.logic_y:
            return self.adjustDirectionNotReverse("UP")
        elif next_tile[1] > self.logic_x:
            return self.adjustDirectionNotReverse("RIGHT")
        else:
            return self.adjustDirectionNotReverse("LEFT")