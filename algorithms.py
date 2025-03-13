from queue import Queue
from heapq import heappop, heappush

def BFSSearch(board, start, end):
    q = Queue()
    q.put(start)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = set()
    tracer = {}

    visited.add(start)

    while (q.qsize() > 0):
        current_pos = q.get()
        if current_pos == end:
            break

        for dx, dy in directions:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3) and (new_pos not in visited):
                q.put(new_pos)
                tracer[new_pos] = current_pos
                visited.add(new_pos)

    return tracer

def UCSSearch(board, start, end):
    visited = set()
    frontier = []
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    tracer = {}
    costs = {start: 0}

    heappush(frontier, start)

    while frontier:
        current_pos = heappop(frontier)
        if current_pos == end:
            break
        
        visited.add(current_pos)

        for dx, dy in directions:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            new_cos = costs[current_pos] + 1

            if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3) and (new_pos not in visited):
                if new_pos not in costs or new_cos < costs[new_pos]:
                    costs[new_pos] = new_cos
                    heappush(frontier, new_pos)
                    tracer[new_pos] = current_pos

    return tracer

def mahattan(curr, end):
    return abs(curr[0] - end[0]) + abs(curr[1] - end[1])

def AStarSearch(board, start, end):
    visited = set()
    frontier = []
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    costs = {start: 0}
    tracer = {}
    heappush(frontier, (0 + mahattan(start, end), start))

    while frontier:
        current_priority, current_pos = heappop(frontier)
        if current_pos == end:
            break
        
        visited.add(current_pos)

        for dx, dy in directions:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            new_cos = costs[current_pos] + 1

            if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3) and (new_pos not in visited):
                if new_pos not in costs or new_cos < costs[new_pos]:
                    costs[new_pos] = new_cos
                    tracer[new_pos] = current_pos

                    priority = new_cos + mahattan(new_pos, end)
                    heappush(frontier, (priority, new_pos))

    return tracer

def DFSSearch(board, start, end):
    stack = [start]  # Stack for DFS
    visited = set()
    tracer = {}  # To track the path

    while stack:
        current_pos = stack.pop()
        if current_pos in visited:
            continue

        visited.add(current_pos)

        if current_pos == end:
            break

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)

            # Check bounds and walkable tiles
            if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] != 1) and (new_pos not in visited):
                stack.append(new_pos)
                tracer[new_pos] = current_pos

    return tracer


def reconstructPath(tracer, start, end):

    path = [end]
    while (start != end):
        end = tracer[end]
        path.append(end)

    path.pop()

    return path[::-1]