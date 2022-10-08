from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        nodesQ = deque()
        nodesQ.append(root)
        while nodesQ:
            q_size = len(nodesQ)
            level_nodes = []
            for _ in range(q_size):
                node = nodesQ.popleft()
                if node:
                    level_nodes.append(node.val)
                    if node.left:
                        nodesQ.append(node.left)
                    if node.right:
                        nodesQ.append(node.right)

            if len(level_nodes) > 0:
                result.appendleft(level_nodes)

        return list(result)