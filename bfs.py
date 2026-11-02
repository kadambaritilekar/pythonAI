from collections import deque

def bfs(grid, start, goal):
    n = len(grid)
    m = len(grid[0])

    q = deque([(start, [start])])
    visited = {start}

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        pos, path = q.popleft()
        r, c = pos

        if pos == goal:
            return path

        for dr, dc in moves:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < n and 0 <= nc < m
                and grid[nr][nc] == 0
                and (nr, nc) not in visited):

                visited.add((nr, nc))
                q.append(((nr, nc), path + [(nr, nc)]))

    return None

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = bfs(grid, start, goal)

if path:
    print("Path Found:")
    for p in path:
        print(p)
    print("Total Steps:", len(path) - 1)
else:
    print("No path exists.")