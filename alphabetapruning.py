# Practical: Alpha-Beta Pruning
#
# Aim:
# To implement Alpha-Beta Pruning to optimise the Minimax algorithm.
#
# Theory:
# MAX tries to maximise the score, while MIN tries to minimise it.
# Alpha stores the best value MAX can guarantee so far.
# Beta stores the best value MIN can guarantee so far.
# When alpha >= beta, the remaining children can be pruned.
#
# Algorithm:
# 1. If the node is a leaf, return its value.
# 2. If it is MAX's turn, find the maximum child value.
# 3. Update alpha with the best value found by MAX.
# 4. If alpha >= beta, stop exploring the remaining children.
# 5. If it is MIN's turn, find the minimum child value.
# 6. Update beta with the best value found by MIN.
# 7. If beta <= alpha, stop exploring the remaining children.
# 8. Return the best value.
#
# Time Complexity:
# Worst case: O(b^d)
# Best case with ideal move ordering: approximately O(b^(d/2))
#
# Space Complexity:
# O(d) auxiliary recursion stack space, excluding the tree.
#
# Advantages:
# 1. Reduces unnecessary node evaluations.
# 2. Produces the same optimal value as Minimax.
#
# Disadvantages:
# 1. Efficiency depends on the order in which children are explored.
# 2. Large game trees may still require substantial computation.
#
# Applications:
# Tic-Tac-Toe, Chess, Checkers, and other adversarial games.

# Game tree: root is MAX; its children are MIN nodes.
tree = [
    [3, 4],
    [2, 7]
]


def alpha_beta(node, is_max, alpha, beta):

    # Base case: if the node is a leaf, return its value.
    if isinstance(node, int):
        return node

    # MAX tries to find the highest value.
    if is_max:
        best = float('-inf')

        for child in node:
            value = alpha_beta(child, False, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            # Prune remaining children if alpha >= beta.
            if alpha >= beta:
                break

        return best

    # MIN tries to find the lowest value.
    else:
        best = float('inf')

        for child in node:
            value = alpha_beta(child, True, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            # Prune remaining children if beta <= alpha.
            if beta <= alpha:
                break

        return best


# Start with MAX; initially, there are no bounds on the score.
result = alpha_beta(tree, True, float('-inf'), float('inf'))

# Display the optimal value.
print("Best value:", result)