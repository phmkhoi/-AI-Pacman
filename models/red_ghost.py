from models.ghosts import Ghost
from queue import PriorityQueue, Queue
from ui.game_map import BOARDS

class RedGhost(Ghost):
    def __init__(self, xCoord, yCoord, target, speed, img):
        super().__init__(xCoord, yCoord, target, speed, img)
        # self.path = self.BFSSearch()

    # Using Mahattan
    def heuristic(self, src, des):
        return abs(src[0] - des[0]) + abs(src[1] - des[1])