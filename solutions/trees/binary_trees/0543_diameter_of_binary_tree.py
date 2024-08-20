from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]
        # def traverse(node):
        #     if not node:
        #         return 0
        #     left = 0
        #     if node.left:
        #         left = 1 + traverse(node.left)
        #     right = 0
        #     if node.right:
        #         right = 1 + traverse(node.right)
        #     diameter[0] = max(diameter[0], left + right)
        #     return max(left, right)

        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            diameter[0] = max(diameter[0], left + right)
            return 1 + max(left, right)

        if root:
            traverse(root)

        return diameter[0]




        