# Practical 11: Game-Playing Agent Using the Minimax Algorithm
#
# Aim:
# To implement the Minimax algorithm for optimal decision-making
# in a two-player game.
#
# Problem Statement:
# Find the best possible value for the MAX player, assuming
# that both MAX and MIN play optimally.
#
# Theory:
# MAX tries to maximise the score, whereas MIN tries to minimise it.
# Minimax evaluates the game tree from the leaf nodes to the root.
#
# Algorithm:
# 1. Accept four leaf values from the user.
# 2. If the current depth reaches the leaf level, return its value.
# 3. If it is MAX's turn, return the maximum of the two children.
# 4. If it is MIN's turn, return the minimum of the two children.
# 5. Repeat recursively until the root value is calculated.
# 6. Display the best value.
#
# Pseudocode:
# MINIMAX(depth, node, is_max, values):
#     IF depth == 2:
#         RETURN values[node]
#
#     IF is_max:
#         RETURN MAX(
#             MINIMAX(depth + 1, node * 2, FALSE, values),
#             MINIMAX(depth + 1, node * 2 + 1, FALSE, values)
#         )
#     ELSE:
#         RETURN MIN(
#             MINIMAX(depth + 1, node * 2, TRUE, values),
#             MINIMAX(depth + 1, node * 2 + 1, TRUE, values)
#         )
#
# Time Complexity: O(2^d), where d is the maximum tree depth.
# Space Complexity: O(d), for the recursive call stack.
#
# Advantages:
# 1. Finds the optimal value when both players play optimally.
# 2. Simple to implement using recursion.
#
# Disadvantages:
# 1. Evaluates many nodes as the game tree grows.
# 2. Assumes both players make optimal decisions.
#
# Applications:
# Tic-Tac-Toe, Chess, Checkers, and other two-player games.
#
# Limitation:
# This implementation uses a fixed binary tree of depth 2
# and exactly four leaf values. It is a simplified demonstration.

def minimax(depth, node, is_max, values):

    # Base case: return the leaf value when depth reaches 2.
    if depth == 2:
        return values[node]

    # MAX player selects the larger value.
    if is_max:
        return max(
            minimax(depth + 1, node * 2, False, values),
            minimax(depth + 1, node * 2 + 1, False, values)
        )

    # MIN player selects the smaller value.
    else:
        return min(
            minimax(depth + 1, node * 2, True, values),
            minimax(depth + 1, node * 2 + 1, True, values)
        )


# Accept four leaf values from the user.
values = list(map(int, input("Enter 4 leaf values: ").split()))

# Ensure that exactly four values are provided.
if len(values) != 4:
    print("Please enter exactly 4 integer values.")

else:
    # Start at depth 0, root node 0, with MAX playing first.
    result = minimax(0, 0, True, values)

    # Display the optimal value for MAX.
    print("Best value:", result)