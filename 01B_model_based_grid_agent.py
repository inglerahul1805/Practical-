# Practical 1B: Model-Based Agent - Grid Navigation with Obstacles
from collections import deque

GRID = [
    ["S", ".", "#", "."],
    [".", ".", "#", "."],
    ["#", ".", ".", "."],
    [".", ".", "#", "G"],
]
ROWS, COLS = len(GRID), len(GRID[0])


def find_position(symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if GRID[r][c] == symbol:
                return (r, c)
    raise ValueError(f"{symbol} not found")


def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            nxt = (nr, nc)
            if (0 <= nr < ROWS and 0 <= nc < COLS
                    and GRID[nr][nc] != "#" and nxt not in visited):
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None


def main():
    start, goal = find_position("S"), find_position("G")
    internal_state = {"known_obstacles": set(), "visited": set()}
    path = bfs(start, goal)

    if path is None:
        print("No path to the goal.")
        return

    print("Grid (# = obstacle, S = start, G = goal):")
    for row in GRID:
        print(" ".join(row))

    print("\nAgent path:")
    for position in path:
        internal_state["visited"].add(position)
        print(position)
    print("Moves required:", len(path) - 1)
    print("Internal state:", internal_state)


if __name__ == "__main__":
    main()
