# Practical 4: A* Search for the 8-Puzzle
import heapq

START = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan(state):
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = GOAL.index(tile)
        r1, c1 = divmod(index, 3)
        r2, c2 = divmod(goal_index, 3)
        distance += abs(r1 - r2) + abs(c1 - c2)
    return distance


def neighbors(state):
    zero = state.index(0)
    r, c = divmod(zero, 3)
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[j] = new_state[j], new_state[zero]
            yield tuple(new_state)


def astar(start, goal):
    # Heap entries: (f, g, state)
    heap = [(manhattan(start), 0, start)]
    parent = {start: None}
    best_g = {start: 0}

    while heap:
        _, g, state = heapq.heappop(heap)
        if g != best_g.get(state):
            continue
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in neighbors(state):
            new_g = g + 1
            if new_g < best_g.get(nxt, float("inf")):
                best_g[nxt] = new_g
                parent[nxt] = state
                heapq.heappush(heap, (new_g + manhattan(nxt), new_g, nxt))
    return None


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


if __name__ == "__main__":
    path = astar(START, GOAL)
    if path:
        print("Solution found in", len(path) - 1, "moves:")
        for state in path:
            print_board(state)
    else:
        print("No solution found.")
