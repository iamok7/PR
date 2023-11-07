def knapsack(W, wt, val, n):
    def bound(node):
        if node.level == n:
            return node.value
        else:
            bound = node.value
            for i in range(node.level + 1, n):
                if wt[i] <= W - node.weight:
                    bound += val[i]
                else:
                    break
            return bound

    class Node:
        def __init__(self, level, weight, value):
            self.level = level
            self.weight = weight
            self.value = value

    root = Node(0, 0, 0)
    queue = [root]
    best_value = 0

    while queue:
        node = queue.pop(0)
        if node.level == n:
            best_value = max(best_value, node.value)
        else:
            if node.weight + wt[node.level] <= W:
                child = Node(node.level + 1, node.weight + wt[node.level], node.value + val[node.level])
                if bound(child) >= best_value:
                    queue.append(child)
            child = Node(node.level + 1, node.weight, node.value)
            if bound(child) >= best_value:
                queue.append(child)

    return best_value


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack(W, wt, val, n))
