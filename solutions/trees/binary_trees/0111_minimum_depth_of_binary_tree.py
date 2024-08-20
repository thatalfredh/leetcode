from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # if not root:
        #     return 0
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)

        # if not root.left and not root.right: # leaf node
        #     return 1
        # if not root.left:
        #     return 1 + right
        # if not root.right:
        #     return 1 + left
        # return 1 + min(left, right)

        min_depth = float("inf")
        if root:
            queue = deque()
            queue.append([root, 1])
            while queue:
                node, d = queue.popleft()
                if not node.left and not node.right:
                    min_depth = min(min_depth, d)
                else:
                    if node.left: queue.append([node.left, d+1])
                    if node.right: queue.append([node.right, d+1])
            return min_depth
        return 0

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None # TreeNode(None)
root.left.right = None # TreeNode(None)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.minDepth(root)
print(result)