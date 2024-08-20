from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ## Recursive Solution:
        # def dfs(node):
        #     if node:
        #         return 1 + max(dfs(node.left), dfs(node.right))
        #     return 0
        # if root:
        #     return dfs(root)
        # else:
        #     return 0

        ## Iterative Solution
        depth = 0
        stack = deque([])
        if root:
            stack.append([root, depth + 1])
            while stack:
                node, d = stack.pop()
                if d > depth:
                    depth = d
                if node.left: stack.append([node.left, d+1])
                if node.right: stack.append([node.right, d+1])
        
        return depth


        