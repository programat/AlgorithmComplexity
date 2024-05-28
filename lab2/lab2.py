import random
import time


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def generate_random_tree(n):
        if n == 0:
            return None
        root = TreeNode(random.randint(1, 100))
        left_size = random.randint(0, n - 1)
        right_size = n - 1 - left_size
        root.left = BinaryTree.generate_random_tree(left_size)
        root.right = BinaryTree.generate_random_tree(right_size)
        return root

    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes_recursive(node.left) + self.count_nodes_recursive(node.right)

    def count_nodes_iterative(self, node):
        if node is None:
            return 0

        count = 0
        stack = [node]

        while stack:
            current = stack.pop()
            count += 1
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return count

    def count_nodes_indirect(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes_helper(node.left) + self.count_nodes_helper(node.right)

    def count_nodes_helper(self, node):
        if node is None:
            return 0
        return self.count_nodes_indirect(node)

    def count_nodes(self, method='recursive'):
        if method == 'recursive':
            return self.count_nodes_recursive(self.root)
        elif method == 'iterative':
            return self.count_nodes_iterative(self.root)
        elif method == 'indirect':
            return self.count_nodes_indirect(self.root)
        else:
            raise ValueError("Unknown method: choose 'recursive', 'iterative', or 'indirect'")


def experimental_complexity():
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    methods = ['recursive', 'iterative', 'indirect']

    for size in sizes:
        tree = BinaryTree(BinaryTree.generate_random_tree(size))

        for method in methods:
            start_time = time.time()
            count = tree.count_nodes(method)
            end_time = time.time()
            print(
                f"Method: {method.capitalize()}, Size: {size}, Count: {count}, Time: {end_time - start_time:.6f} seconds")


if __name__ == '__main__':
    experimental_complexity()

# print(f"Tree size: {size}, Node count: {node_count}, Time: {end_time - start_time:.6f} seconds")
