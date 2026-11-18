# Practical 8: Goal Stack Planning for Blocks World
# This example builds a plan for: A on table, B on C, C on table.
# State representation: dictionary block -> support ("table" or another block).

def clear_block(state, block):
    return all(support != block for support in state.values())


def apply_action(state, action):
    name, block, destination = action
    if name == "MOVE":
        state[block] = destination


def goal_stack_plan(initial, goals):
    state = dict(initial)
    plan = []
    goal_stack = list(reversed(goals))

    while goal_stack:
        goal = goal_stack.pop()
        block, desired_support = goal

        if state.get(block) == desired_support:
            continue

        # A block can be moved only when it is clear.
        if not clear_block(state, block):
            above = next(b for b, support in state.items() if support == block)
            goal_stack.append(goal)
            goal_stack.append((above, "table"))
            continue

        # Destination must be clear if it is another block.
        if desired_support != "table" and not clear_block(state, desired_support):
            above = next(b for b, support in state.items()
                         if support == desired_support)
            goal_stack.append(goal)
            goal_stack.append((above, "table"))
            continue

        action = ("MOVE", block, desired_support)
        apply_action(state, action)
        plan.append(action)

    return plan, state


if __name__ == "__main__":
    # Initial: A on B, B on table, C on table.
    initial_state = {"A": "B", "B": "table", "C": "table"}
    # Goal: A on table, B on C, C on table.
    goals = [("A", "table"), ("B", "C"), ("C", "table")]

    actions, final_state = goal_stack_plan(initial_state, goals)
    print("Plan:")
    for step, action in enumerate(actions, 1):
        print(step, action)
    print("Final state:", final_state)
