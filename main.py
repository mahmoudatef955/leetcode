from __future__ import print_function

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    if root is None:
        return []
    all_paths = []
    find_path_rec(root, sum, all_paths, [])
    return all_paths


def find_path_rec(current_node, sum, result, current_path):
    if current_node is None:
        return

    current_path.append(current_node.val)
    if (
        current_node.left is None
        and current_node.right is None
        and current_node.val == sum
    ):
        result.append(list(current_path))
    else:
        # current_path.append(root.val)
        find_path_rec(current_node.left, sum - current_node.val, result, current_path)
        find_path_rec(current_node.right, sum - current_node.val, result, current_path)

    del current_path[-1]


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


if __name__ == "__main__":
    main()
