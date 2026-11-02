# AI Practical 6: 8-Queens Problem
# Aim: To place 8 queens on an 8x8 chessboard so that no two
# queens attack each other, using backtracking.

# Algorithm:
# 1. Start with an empty board.
# 2. Try placing a queen in each column of the current row.
# 3. Check whether the position is safe from column and diagonal attacks.
# 4. If safe, place the queen and move to the next row.
# 5. If the next row has no safe position, remove the previous queen
#    and try another column.
# 6. Repeat until all 8 queens are placed.
# 7. Display the solution if one is found.

# Pseudocode:
# START
# Initialize board with -1 for all 8 rows.
# FUNCTION is_safe(board, row, col):
#     Check previous rows for column conflicts.
#     Check both diagonals for conflicts.
#     Return True if the position is safe; otherwise False.
# FUNCTION solve(board, row):
#     IF row == 8:
#         Return True.
#     FOR each column from 0 to 7:
#         IF position is safe:
#             Place queen.
#             IF solve(next row) succeeds:
#                 Return True.
#             Remove queen (backtrack).
#     Return False.
# Call solve and display the board.

def is_safe(board, row, col):
    # Check whether a queen in the same column exists above.
    for i in range(row):
        if board[i] == col:
            return False

    # Check the upper-left diagonal.
    for i in range(row):
        if board[i] - i == col - row:
            return False

    # Check the upper-right diagonal.
    for i in range(row):
        if board[i] + i == col + row:
            return False

    # The position is safe if no conflict is found.
    return True


def solve(board, row):
    # Base case: all 8 queens have been placed.
    if row == 8:
        return True

    # Try placing a queen in every column of the current row.
    for col in range(8):
        if is_safe(board, row, col):
            # Place the queen in the current row.
            board[row] = col

            # Move to the next row.
            if solve(board, row + 1):
                return True

            # Backtrack: remove the queen and try another column.
            board[row] = -1

    # No valid position was found in this row.
    return False


# Main program: -1 means no queen is placed in that row.
board = [-1] * 8

if solve(board, 0):
    print("Solution to the 8-Queens Problem:")

    # Display the chessboard.
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists.")


# Time Complexity: O(N!) in the worst case for the standard
# row-by-row backtracking approach, where N is the board size.
# For this practical, N = 8.

# Space Complexity: O(N) auxiliary space for the board and
# recursive call stack, excluding the displayed output.

# Optimization:
# 1. Use sets to track occupied columns and diagonals.
# 2. This reduces repeated safety checks and can improve runtime.
# 3. The current version is simpler and follows the approach
#    given in the practical PDF.

# Advantages:
# 1. Avoids exploring complete arrangements that contain conflicts.
# 2. Demonstrates backtracking and constraint satisfaction.
# 3. Easy to understand and extend to the N-Queens Problem.

# Disadvantages:
# 1. May explore many arrangements before finding a solution.
# 2. Repeated safety checks can increase execution time for larger boards.
# 3. This recursive implementation requires understanding recursion.