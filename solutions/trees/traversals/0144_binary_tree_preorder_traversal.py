# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def preorder_traverse(root):
            if root:
                values.append(root.val)
                preorder_traverse(root.left)
                preorder_traverse(root.right)
        preorder_traverse(root)
        return values
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.preorderTraversal(root)
print(result)