# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        ltr: bool = True
        queue = deque()
        queue.append(root)
        while queue:
            l_size = len(queue)
            level = []
            for _ in range(l_size):
                node = queue.popleft()
                if node:
                    level.append(node.val) if ltr else level.insert(0, node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            result.append(level)
            ltr = not ltr

        return result
