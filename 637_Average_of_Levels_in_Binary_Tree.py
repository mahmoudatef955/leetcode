# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            l_size = len(queue)
            level_nodes = []
            for _ in range(l_size):
                node = queue.popleft()
                if node:
                    level_nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(sum(level_nodes) / float(len(level_nodes)))
        return result
