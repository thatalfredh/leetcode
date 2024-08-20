from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        queue = deque([])

        if root:
            queue.append(root)
            while queue:
                level_vals = []
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    level_vals.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                values.append(level_vals)

        return values
                

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.levelOrder(root)
print(result)        