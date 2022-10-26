from __future__ import print_function


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):

    return find_path_rec(root, sequence)


def find_path_rec(node, sequence):
    if node is None:
        return False

    elif len(sequence) == 0 or node.val != sequence[0]:
        return False

    elif (
        node.left is None
        and node.right is None
        and len(sequence) == 1
        and node.val == sequence[0]
    ):
        return True
    else:
        return find_path_rec(node.left, sequence[1:]) or find_path_rec(
            node.right, sequence[1:]
        )


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


if __name__ == "__main__":
    main()
