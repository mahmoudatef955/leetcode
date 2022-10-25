from __future__ import print_function


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    all_sum = find_sum_of_path_numbers_rec(root, 0)
    return all_sum


def find_sum_of_path_numbers_rec(node, current_sum):
    # current_num = current_num + str(node.val)
    # current_num.append(str(node.val))
    # if node.left is None and node.right is None:
    #     all_sum.append(int(''.join(list(current_num))))
    # if node.left:
    #     find_sum_of_path_numbers_rec(node.left, current_num, all_sum)
    # if node.right:
    #     find_sum_of_path_numbers_rec(node.right, current_num, all_sum)
    #
    # del current_num[-1]
    if node is None:
        return 0
    current_sum = current_sum * 10 + node.val
    if node.left is None and node.right is None:
        return current_sum
    return find_sum_of_path_numbers_rec(node.left, current_sum) + find_sum_of_path_numbers_rec(node.right, current_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


if __name__ == "__main__":
    main()
