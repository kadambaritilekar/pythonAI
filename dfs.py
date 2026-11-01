
# Practical: Solve the Water Jug Problem using DFS

def dfs(a, b, visited, path):

    # Goal condition: obtain exactly 2 liters
    if a == 2 or b == 2:
        path.append((a, b))
        return True

    # Avoid revisiting the same state
    if (a, b) in visited:
        return False

    visited.add((a, b))
    path.append((a, b))

    # Generate all possible next states
    states = [
        (4, b),                                  # Fill Jug A
        (a, 3),                                  # Fill Jug B
        (0, b),                                  # Empty Jug A
        (a, 0),                                  # Empty Jug B
        (a - min(a, 3 - b), b + min(a, 3 - b)),  # Pour A into B
        (a + min(b, 4 - a), b - min(b, 4 - a))   # Pour B into A
    ]

    # Explore each state using DFS
    for new_a, new_b in states:
        if dfs(new_a, new_b, visited, path):
            return True

    # Backtrack if no solution is found
    path.pop()
    return False


# Main program
visited = set()
path = []

if dfs(0, 0, visited, path):
    print("Solution:")
    for state in path:
        print(state)
else:
    print("No solution found.")


# ALGORITHM
# 1. Start with both jugs empty: (0, 0).
# 2. Check whether either jug contains exactly 2 liters.
# 3. If the goal is reached, return True.
# 4. If the state was already visited, return False.
# 5. Mark the state as visited and add it to the path.
# 6. Generate all six possible next states.
# 7. Explore each next state recursively using DFS.
# 8. If a branch fails, remove its state from the path.
# 9. Stop when a solution is found or all states are explored.


# PSEUDOCODE
# DFS(a, b):
#     If a == 2 or b == 2:
#         Add (a, b) to path
#         Return True
#
#     If (a, b) is visited:
#         Return False
#
#     Mark (a, b) as visited
#     Add (a, b) to path
#
#     For each possible next state:
#         If DFS(next state) returns True:
#             Return True
#
#     Remove current state from path
#     Return False


# TIME COMPLEXITY: O(V + E)
# V = Number of reachable states
# E = Number of transitions between states
#
# SPACE COMPLEXITY: O(V)
# Stores visited states and the recursion stack.
#
# WHY DOES IT WORK?
# DFS explores possible states until it reaches the goal.
# The visited set prevents repeated exploration.
# Backtracking removes unsuccessful states from the path.
#
# POSSIBLE IMPROVEMENT:
# BFS can find a solution using the fewest operations
# when all operations have equal cost.
