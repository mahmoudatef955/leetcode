# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        all_paths = []
        find_path_rec(root, targetSum, all_paths, [])
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
