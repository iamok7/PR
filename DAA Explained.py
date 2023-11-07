def knapsack(W, wt, val, n):
    """
    Solves the 0-1 Knapsack problem using the branch and bound algorithm.

    Args:
        W (int): The maximum weight of the knapsack.
        wt (list): A list of the weights of the items.
        val (list): A list of the values of the items.
        n (int): The number of items.

    Returns:
        int: The maximum value of a subset of items with a total weight of at most W.
    """

    def bound(node):
        """
        Calculates a lower bound on the value of a node in the search tree.

        Args:
            node (Node): The node to calculate the bound for.

        Returns:
            int: The lower bound on the value of the node.
        """
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
        """
        Represents a node in the search tree.

        Attributes:
            level (int): The level of the node in the tree.
            weight (int): The weight of the items that have been selected so far.
            value (int): The value of the items that have been selected so far.
        """

        def __init__(self, level, weight, value):
            self.level = level
            self.weight = weight
            self.value = value

    root = Node(0, 0, 0)
    """
    Creates a root node with a level of 0, a weight of 0, and a value of 0.
    """

    queue = [root]
    """
    Creates a queue to store the nodes to be processed.
    """

    best_value = 0
    """
    Initializes the best value found so far.
    """

    while queue:
        node = queue.pop(0)
        """
        Removes the first node from the queue.
        """

        if node.level == n:
            """
            If the node is a leaf node, update the best value.
            """
            best_value = max(best_value, node.value)
        else:
            """
            If the node is not a leaf node, create two child nodes.
            """
            if node.weight + wt[node.level] <= W:
                """
                Create a child node by including the item at the current level in the knapsack.
                """
                child = Node(node.level + 1, node.weight + wt[node.level], node.value + val[node.level])
                """
                Calculate the bound for the child node.
                """
                bound_value = bound(child)
                """
                If the bound for the child node is greater than or equal to the best value, add the child node to the queue.
                """
                if bound_value >= best_value:
                    queue.append(child)

            """
            Create a child node by excluding the item at the current level from the knapsack.
            """
            child = Node(node.level + 1, node.weight, node.value)
            """
            Calculate the bound for the child node.
            """
            bound_value = bound(child)
            """
            If the bound for the child node is greater than or equal to the best value, add the child node to the queue.
            """
            if bound_value >= best_value:
                queue.append(child)

    return best_value
    """
    Returns the best value found so far.
    """

if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack(W, wt, val, n))
