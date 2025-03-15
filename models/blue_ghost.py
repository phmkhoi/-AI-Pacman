from models.ghosts import Ghost
from algorithms import BFSSearch, getRandomMove, reconstructPath, BFSSearchCountExpandNodes
import tracemalloc
class BlueGhost(Ghost):
    def __init__(self, x_2DCoord, y_2DCoord, target, speed, img, status, direction, board, in_cage):
        super().__init__(x_2DCoord, y_2DCoord, target, speed, img, status, direction, board, in_cage)

    def getDirection(self):
        if self.status == "CHASE":
            tracer = BFSSearch(self.board, (self.logic_y, self.logic_x), self.target)
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

    def getMemory(self, target):
        self.target = target
        if self.status == "CHASE":
             if not self.in_cage:
                if self.checkTurnable() or self.checkCollision():
                    tracemalloc.start()
                    BFSSearch(self.board, (self.logic_y, self.logic_x), self.target)
                    memory = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    return memory[1]
        
        return 0
    
    def getExpandNodes(self, target):
        self.target = target
        if self.status == "CHASE":
             if not self.in_cage:
                if self.checkTurnable() or self.checkCollision():
                   count_nodes = BFSSearchCountExpandNodes(self.board, (self.logic_y, self.logic_x), self.target)
                   return count_nodes
        
        return 0

    def getPath(self):
        tracer = BFSSearch(self.board, (self.logic_y, self.logic_x), self.target)
        path = reconstructPath(tracer, (self.logic_y, self.logic_x), self.target)
        return path