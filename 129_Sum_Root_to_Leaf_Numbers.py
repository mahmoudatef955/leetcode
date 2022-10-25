# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        all_sum = self.find_sum_of_path_numbers_rec(root, 0)
        return all_sum

    def find_sum_of_path_numbers_rec(self, node, current_sum):
        if node is None:
            return 0
        current_sum = current_sum * 10 + node.val
        if node.left is None and node.right is None:
            return current_sum
        return self.find_sum_of_path_numbers_rec(node.left, current_sum) + self.find_sum_of_path_numbers_rec(node.right,
                                                                                                             current_sum)
