# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Intuitive Recursive
        values = []
        def traverse_inorder(root):
            if root:
                traverse_inorder(root.left)
                values.append(root.val)
                traverse_inorder(root.right)
        traverse_inorder(root)
        return values
        
        # Iterative 1: Mine
        values = []
        stack = deque([])
        if root:
            stack.append(root.right)
            stack.append(root.value)
            stack.append(root.left)
            while stack:
                node = stack.pop()
                if type(node) != TreeNode: values.append(node)
                else:
                    stack.append(node.right)
                    stack.append(node.value)
                    stack.append(node.left)
        return values

        # Iterative 2: Other People
        traversal = []
        node = root
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node.val)
                node = node.right
                
        return traversal

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.inorderTraversal(root)
print(result)

