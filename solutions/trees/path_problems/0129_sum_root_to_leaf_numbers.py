from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, s):
            if not node: return 0
            s = s * 10 + node.val
            if not node.left and not node.right:
                return s
            return dfs(node.left, s) + dfs(node.right, s)

        return dfs(root, 0)

        