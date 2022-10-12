from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        queue = deque()
        queue.append(root)
        while root:
            l_size = len(queue)
            for _ in range(l_size):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            depth = depth + 1

        return depth
