# Practical 3: BFS for a Blocks World Planning Problem
# A state is a tuple of stacks; the last block in each stack is on top.

from collections import deque

START = (("A", "B"), ("C",))
GOAL = (("A",), ("B", "C"))


def successors(state):
    stacks = [list(s) for s in state]
    result = []

    for i, source in enumerate(stacks):
        if not source:
            continue
        block = source[-1]

        # Move the top block to the table (a new stack).
        new_stacks = [s[:] for s in stacks]
        new_stacks[i].pop()
        new_stacks = [s for s in new_stacks if s]
        new_stacks.append([block])
        result.append(tuple(sorted(tuple(s) for s in new_stacks)))

        # Move the top block onto the top of another stack.
        for j in range(len(stacks)):
            if i == j:
                continue
            new_stacks = [s[:] for s in stacks]
            new_stacks[i].pop()
            new_stacks[j].append(block)
            new_stacks = [s for s in new_stacks if s]
            result.append(tuple(sorted(tuple(s) for s in new_stacks)))

    # Remove duplicate states.
    return list(dict.fromkeys(result))


def bfs(start, goal):
    start = tuple(sorted(tuple(s) for s in start))
    goal = tuple(sorted(tuple(s) for s in goal))
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for nxt in successors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None


if __name__ == "__main__":
    solution = bfs(START, GOAL)
    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("Goal state cannot be reached.")
