from queue import Queue
from heapq import heappop, heappush
import random

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
    visited.add(start)

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
                    visited.add(new_pos)

        min_cost = costs[frontier[0]]
        check_min_cost = 0
        for i in range(len(frontier)):
            if min_cost > costs[frontier[i]]:
                min_cost = costs[frontier[i]]
                check_min_cost = i
        
        if check_min_cost != 0:
            tmp = frontier[0]
            frontier[0] = frontier[check_min_cost]
            frontier[check_min_cost] = tmp
        
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

def DLSSearch(board, start, end, depth_limit):
    stack = [(start, 0)]  # Stack for DFS
    visited = set()
    tracer = {}
    
    while stack:
        current_pos, depth = stack.pop()
        if current_pos in visited:
            continue

        visited.add(current_pos)

        if current_pos == end:
            return tracer

        if depth < depth_limit:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_pos = (current_pos[0] + dx, current_pos[1] + dy)

                # Check bounds and walkable tiles
                if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3) and (new_pos not in visited):
                    stack.append((new_pos, depth + 1))
                    tracer[new_pos] = current_pos
                    
    return None

def IDSSearch(board, start, end):
    tracer = {}

    depth = 0
    while True:
        if tracer:
            return tracer

        tracer = DLSSearch(board, start, end, depth)
        depth += 1

def BFSSearchCountExpandNodes(board, start, end):
    q = Queue()
    q.put(start)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = set()
    count_nodes = 0

    visited.add(start)

    while (q.qsize() > 0):
        current_pos = q.get()
        count_nodes += 1
        if current_pos == end:
            break

        for dx, dy in directions:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3) and (new_pos not in visited):
                q.put(new_pos)
                visited.add(new_pos)

    return count_nodes

def UCSSearchCountExpandNodes(board, start, end):
    visited = set()
    frontier = []
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    costs = {start: 0}
    count_nodes = 0

    heappush(frontier, start)
    visited.add(start)

    while frontier:
        current_pos = heappop(frontier)
        count_nodes += 1
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
                    visited.add(new_pos)

        min_cost = costs[frontier[0]]
        check_min_cost = 0
        for i in range(len(frontier)):
            if min_cost > costs[frontier[i]]:
                min_cost = costs[frontier[i]]
                check_min_cost = i
        
        if check_min_cost != 0:
            tmp = frontier[0]
            frontier[0] = frontier[check_min_cost]
            frontier[check_min_cost] = tmp
        
    return count_nodes 

def mahattan(curr, end):
    return abs(curr[0] - end[0]) + abs(curr[1] - end[1])

def AStarSearchCountExpandNodes(board, start, end):
    visited = set()
    frontier = []
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    costs = {start: 0}
    count_nodes = 0

    heappush(frontier, (0 + mahattan(start, end), start))

    while frontier:
        current_priority, current_pos = heappop(frontier)
        count_nodes += 1

        if current_pos == end:
            break
        
        visited.add(current_pos)

        for dx, dy in directions:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            new_cos = costs[current_pos] + 1

            if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3) and (new_pos not in visited):
                if new_pos not in costs or new_cos < costs[new_pos]:
                    costs[new_pos] = new_cos

                    priority = new_cos + mahattan(new_pos, end)
                    heappush(frontier, (priority, new_pos))

    return count_nodes

def DLSSearchCountExpandNodes(board, start, end, depth_limit, count_nodes):
    stack = [(start, 0)]  # Stack for DFS
    visited = set()
    tracer = {}
    
    while stack:
        current_pos, depth = stack.pop()
        count_nodes += 1
        if current_pos in visited:
            continue

        visited.add(current_pos)

        if current_pos == end:
            return tracer, count_nodes

        if depth < depth_limit:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_pos = (current_pos[0] + dx, current_pos[1] + dy)

                # Check bounds and walkable tiles
                if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3) and (new_pos not in visited):
                    stack.append((new_pos, depth + 1))
                    tracer[new_pos] = current_pos
                    
    return None, 0

def IDSSearchCountExpandNodes(board, start, end):
    tracer = {}
    count_nodes = 0
    depth = 0
    while True:
        if tracer:
            return count_nodes

        tracer, count_nodes = DLSSearchCountExpandNodes(board, start, end, depth, count_nodes)
        depth += 1

def getRandomMove(board, cur_pos):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    possible_moves = []

    for dx, dy in directions:
        new_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
        if (0 <= new_pos[0] < len(board)) and (0 <= new_pos[1] < len(board[0])) and (board[new_pos[0]][new_pos[1]] < 3):
            possible_moves.append(new_pos)

    return possible_moves[random.randint(0, len(possible_moves) - 1)]


def reconstructPath(tracer, start, end):

    path = [end]
    while (start != end):
        end = tracer[end]
        path.append(end)

    path.pop()

    return path[::-1]