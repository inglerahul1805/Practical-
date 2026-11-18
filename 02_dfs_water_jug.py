# Practical 2: DFS for the Water Jug Problem

def water_jug_dfs(capacity_a, capacity_b, target):
    start = (0, 0)
    stack = [(start, [start])]
    visited = set()

    while stack:
        (a, b), path = stack.pop()
        if (a, b) in visited:
            continue
        visited.add((a, b))

        if a == target or b == target:
            return path

        transfer_a_to_b = min(a, capacity_b - b)
        transfer_b_to_a = min(b, capacity_a - a)

        next_states = [
            (capacity_a, b),                         # Fill A
            (a, capacity_b),                         # Fill B
            (0, b),                                  # Empty A
            (a, 0),                                  # Empty B
            (a - transfer_a_to_b, b + transfer_a_to_b),
            (a + transfer_b_to_a, b - transfer_b_to_a),
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state, path + [state]))

    return None


if __name__ == "__main__":
    # Classic example: 4-litre and 3-litre jugs; obtain 2 litres.
    solution = water_jug_dfs(4, 3, 2)
    if solution:
        print("Steps (Jug A, Jug B):")
        for step, state in enumerate(solution):
            print(f"{step}: {state}")
    else:
        print("No solution found.")
