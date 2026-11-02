
# AI Practical : 4x4 Sudoku Solver Using Backtracking
#
# Aim:
# Solve a 4x4 Sudoku puzzle using backtracking.
#
# Algorithm:
# 1. Find an empty cell represented by 0.
# 2. Try digits from 1 to 4.
# 3. Check the row, column, and 2x2 subgrid.
# 4. If valid, place the digit and solve the remaining grid recursively.
# 5. If the recursive call fails, reset the cell to 0 and try another digit.
# 6. If no empty cells remain, the puzzle is solved.
#
# Pseudocode:
# FUNCTION is_valid(grid, row, col, num):
#     If num exists in the row or column, return False.
#     Find the top-left corner of the 2x2 subgrid.
#     If num exists in the subgrid, return False.
#     Return True.
#
# FUNCTION solve_sudoku(grid):
#     Find an empty cell.
#     If no empty cell exists, return True.
#     For num from 1 to 4:
#         If num is valid:
#             Place num in the cell.
#             If solve_sudoku(grid) succeeds, return True.
#             Reset the cell to 0 (backtrack).
#     Return False.
#
# Time Complexity:
# O(4^N) as a simple upper bound, where N is the number
# of empty cells. Constraint checks prune invalid choices.
#
# Space Complexity:
# O(N) auxiliary space for the recursive call stack,
# excluding the fixed-size grid.
#
# Optimization Notes:
# - Select the empty cell with the fewest valid candidates first.
# - Use sets to track occupied rows, columns, and subgrids.
#
# Advantages:
# - Small and easy to understand.
# - Clearly demonstrates recursion and backtracking.
#
# Disadvantages:
# - May explore many candidate placements.
# - This implementation is specifically configured for 4x4 Sudoku.


def is_valid(grid, row, col, num):
    # Check the current row.
    for c in range(4):
        if grid[row][c] == num:
            return False

    # Check the current column.
    for r in range(4):
        if grid[r][col] == num:
            return False

    # Find the top-left corner of the 2x2 subgrid.
    box_row = (row // 2) * 2
    box_col = (col // 2) * 2

    # Check the 2x2 subgrid.
    for r in range(box_row, box_row + 2):
        for c in range(box_col, box_col + 2):
            if grid[r][c] == num:
                return False

    return True


def solve_sudoku(grid):
    # Find an empty cell.
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:

                # Try digits from 1 to 4.
                for num in range(1, 5):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        # Solve the remaining cells.
                        if solve_sudoku(grid):
                            return True

                        # Backtrack if the choice fails.
                        grid[row][col] = 0

                # No digit works in this cell.
                return False

    # No empty cells remain.
    return True


def print_grid(grid):
    for row in range(4):
        for col in range(4):
            print(grid[row][col], end=" ")
        print()


# Zero represents an empty cell.
grid = [
    [1, 0, 0, 4],
    [0, 4, 1, 0],
    [0, 1, 4, 0],
    [4, 0, 0, 1]
]

print("Original Sudoku:")
print_grid(grid)

if solve_sudoku(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
else:
    print("\nNo solution exists.")
