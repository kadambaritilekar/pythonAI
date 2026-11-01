# AI Practical 4: Robot Path Planning Using BFS
# Aim: To find the shortest path from a start position to a goal
#      position in a grid containing obstacles using BFS.

# Algorithm:
# 1. Initialize a queue with the starting position.
# 2. Mark the starting position as visited.
# 3. Remove a position from the front of the queue.
# 4. If it is the goal, reconstruct and return the path.
# 5. Otherwise, explore its valid neighbouring positions.
# 6. Mark each valid, unvisited neighbour as visited and add it
#    to the queue.
# 7. Repeat until the goal is found or the queue becomes empty.
# 8. If the queue becomes empty, report that no path exists.

# Pseudocode:
# START
# Initialize queue, visited set, and parent dictionary.
# WHILE queue is not empty:
#     Remove the first position from the queue.
#     IF current position is the goal:
#         Reconstruct and return the path.
#     FOR each neighbouring position:
#         IF neighbour is valid, free, and unvisited:
#             Mark neighbour as visited.
#             Store its parent.
#             Add neighbour to the queue.
# RETURN no path found.
# END

from collections import deque


def bfs(grid, start, goal):
    # Get the number of rows and columns in the grid.
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the queue, visited set, and parent dictionary.
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # Possible movements: up, down, left, and right.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Perform BFS until the queue becomes empty.
    while queue:
        # Remove the first position (FIFO order).
        current = queue.popleft()

        # If the goal is reached, reconstruct the shortest path.
        if current == goal:
            path = []
            position = current

            # Trace the path backwards using the parent dictionary.
            while position is not None:
                path.append(position)
                position = parent[position]

            # Reverse the path to obtain start-to-goal order.
            path.reverse()
            return path

        # Get the current row and column.
        row, col = current

        # Explore all four neighbouring positions.
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            neighbour = (new_row, new_col)

            # Check boundaries, obstacles, and previously visited cells.
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == 0
                and neighbour not in visited
            ):
                # Mark the neighbour as visited.
                visited.add(neighbour)

                # Store its parent for path reconstruction.
                parent[neighbour] = current

                # Add the neighbour to the queue.
                queue.append(neighbour)

    # Return None if the goal is unreachable.
    return None


# Grid representation: 0 = free cell, 1 = obstacle.
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Define the start and goal as (row, column) coordinates.
start = (0, 0)
goal = (4, 4)

# Execute BFS to find the shortest path.
path = bfs(grid, start, goal)

# Display the path and number of moves.
if path is not None:
    print("Shortest path found:")
    print(" -> ".join(map(str, path)))
    print("Number of moves:", len(path) - 1)

    # Create a copy of the grid to display the path.
    display_grid = [row[:] for row in grid]

    # Mark intermediate path cells with '*'.
    for row, col in path:
        if (row, col) != start and (row, col) != goal:
            display_grid[row][col] = "*"

    # Mark the start and goal positions.
    display_grid[start[0]][start[1]] = "S"
    display_grid[goal[0]][goal[1]] = "G"

    print("\nGrid with path:")
    for row in display_grid:
        print(" ".join(map(str, row)))

else:
    print("No path found. The goal is unreachable.")


# Time Complexity: O(R * C)
# Each grid cell is visited at most once, where R is the number
# of rows and C is the number of columns.

# Space Complexity: O(R * C)
# The queue, visited set, and parent dictionary can store up to
# R * C cells.

# Optimization:
# 1. Using collections.deque makes queue operations efficient.
# 2. Marking cells visited when enqueued prevents duplicate entries.
# 3. Storing parents avoids copying the complete path at every step.
# 4. BFS is suitable for equal-cost movements. For large grids,
#    A* search may explore fewer cells when a suitable heuristic
#    is available.

# Advantages:
# 1. Finds the shortest path when all movements have equal cost.
# 2. Finds a solution if a reachable goal exists.
# 3. Handles obstacles and grid boundaries.

# Disadvantages:
# 1. Can consume considerable memory for large grids.
# 2. May explore many cells that are not part of the final path.
# 3. Does not guarantee the minimum-cost path when movement costs differ.