# from models.ghosts import Ghost
# from collections import deque
# from ui.game_map import BOARDS, COLUMN_AMOUNT, ROW_AMOUNT

# class RedGhost(Ghost):
#     def __init__(self, xCoord, yCoord, target, speed, img):
#         super().__init__(xCoord, yCoord, target, speed, img)
#         # self.path = self.FindPath()

#     # Using Mahattan
#     # def heuristic(self, src, des):
#     #     return abs(src[0] - des[0]) + abs(src[1] - des[1])
    
#     # Using BFS
#     def FindPath(self):
#         frontier = [(self.x, self.y)]
#         visited = [(self.x, self.y)]
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         path = {}

#         while frontier:
#             currCell = frontier.pop()
#             if currCell == self.target:
#                 break

#             for (dx, dy) in directions:
#                 u, v = currCell[0] + dx, currCell[1] + dy

#                 if (0 <= u < ROW_AMOUNT) and (0 <= v < COLUMN_AMOUNT) and ((u, v) not in visited) and BOARDS[u][v] < 3:
#                     frontier.append((u, v))
#                     visited.append((u, v))
#                     path[(u, v)] = currCell

#         fwdpath = []
#         cell = self.target
#         while cell != (self.x, self.y):
#             fwdpath.append(cell)
#             cell = path[cell]

#         return fwdpath[::-1]