from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def traverse_postorder(root):
            if root:
                traverse_postorder(root.left)
                traverse_postorder(root.right)
                values.append(root.val)
        traverse_postorder(root)
        return values
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.postorderTraversal(root)
print(result)