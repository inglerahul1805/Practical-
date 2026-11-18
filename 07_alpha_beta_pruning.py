# Practical 7: Adversarial Search using Minimax and Alpha-Beta Pruning
# Example game tree. MAX chooses the largest value; MIN chooses the smallest.

def alphabeta(node, depth, alpha, beta, maximizing):
    if isinstance(node, int):
        return node

    if maximizing:
        value = float("-inf")
        for child in node:
            value = max(value, alphabeta(child, depth + 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                print("Pruned remaining MAX branch at depth", depth)
                break
        return value
    else:
        value = float("inf")
        for child in node:
            value = min(value, alphabeta(child, depth + 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                print("Pruned remaining MIN branch at depth", depth)
                break
        return value


if __name__ == "__main__":
    # Root is MAX; next level MIN; leaves are utility values.
    tree = [
        [3, 5, 6],
        [1, 2, 9],
        [0, -1, 4]
    ]
    result = alphabeta(tree, 0, float("-inf"), float("inf"), True)
    print("Best value for MAX:", result)
