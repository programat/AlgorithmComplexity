import time
import random


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node({self.value})'


count_nodes_recursive = lambda node: \
    (1 + count_nodes_recursive(node.left) + count_nodes_recursive(node.right)) if node else 0


def count_nodes_iterative(node):
    if node is None: return 0

    stack = [node]
    count = 0
    while stack:
        node = stack.pop()
        if node:
            count += 1
            stack.append(node.left)
            stack.append(node.right)
    return count


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes_helper(node.left) + count_nodes_helper(node.right)


def count_nodes_helper(node):
    if node is None:
        return 0
    return count_nodes(node)


def generate_random_tree(n):
    if n == 0:
        return None
    root = TreeNode(random.randint(1, 100))
    left_size = random.randint(0, n - 1)
    right_size = n - 1 - left_size
    root.left = generate_random_tree(left_size)
    root.right = generate_random_tree(right_size)
    return root


def experimental_complexity():
    sizes = [10, 100, 1000, 10000, 10000000]
    for size in sizes:
        tree = generate_random_tree(size)

        start_time = time.time()
        node_count = count_nodes_recursive(tree)
        end_time = time.time()
        print(f"Recursive: Size = {size}, Node count: {node_count}, Time = {end_time - start_time:.6f} seconds")
        start_time = time.time()
        node_count = count_nodes_iterative(tree)
        end_time = time.time()
        print(f"Iterative: Size = {size}, Node count: {node_count}, Time = {end_time - start_time:.6f} seconds")
        start_time = time.time()
        node_count = count_nodes(tree)
        end_time = time.time()
        print(f"Indirect: Size = {size}, Node count: {node_count}, Time = {end_time - start_time:.6f} seconds")


if __name__ == '__main__':
    experimental_complexity()

# print(f"Tree size: {size}, Node count: {node_count}, Time: {end_time - start_time:.6f} seconds")
