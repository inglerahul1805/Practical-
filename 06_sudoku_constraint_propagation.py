# Practical 6: Sudoku Solver using Constraint Propagation + Backtracking
# Use 0 for an empty cell.

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def candidates(board, row, col):
    used = set(board[row])
    used.update(board[r][col] for r in range(9))
    br, bc = (row // 3) * 3, (col // 3) * 3
    for r in range(br, br + 3):
        for c in range(bc, bc + 3):
            used.add(board[r][c])
    return set(range(1, 10)) - used


def propagate(board):
    """Repeatedly place cells that have exactly one possible value."""
    changed = True
    while changed:
        changed = False
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    options = candidates(board, r, c)
                    if not options:
                        return False
                    if len(options) == 1:
                        board[r][c] = options.pop()
                        changed = True
    return True


def solve(board):
    if not propagate(board):
        return False

    best_cell = None
    best_options = None
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                options = candidates(board, r, c)
                if not options:
                    return False
                if best_options is None or len(options) < len(best_options):
                    best_cell, best_options = (r, c), options

    if best_cell is None:
        return True

    r, c = best_cell
    for value in sorted(best_options):
        copy = [row[:] for row in board]
        copy[r][c] = value
        if solve(copy):
            for i in range(9):
                board[i] = copy[i]
            return True
    return False


if __name__ == "__main__":
    if solve(grid):
        for row in grid:
            print(*row)
    else:
        print("No solution exists.")
