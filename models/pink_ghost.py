from models.ghosts import Ghost, IMAGE_OFFSET, IMAGE_SCALE
from algorithms import AStarSearch, reconstructPath

class PinkGhost(Ghost):
    def __init__(self, x_2DCoord, y_2DCoord, target, speed, img, direction, board, in_cage):
        super().__init__(x_2DCoord, y_2DCoord, target, speed, img, direction, board, in_cage)

    def getDirection(self):
        tracer = AStarSearch(self.board, (self.logic_y, self.logic_x), self.target)
        path = reconstructPath(tracer, (self.logic_y, self.logic_x), self.target)

        next_tile = path[0]

        if next_tile[0] > self.logic_y:
            return "DOWN"
        elif next_tile[0] < self.logic_y:
            return "UP"
        elif next_tile[1] > self.logic_x:
            return "RIGHT"
        else:
            return "LEFT"