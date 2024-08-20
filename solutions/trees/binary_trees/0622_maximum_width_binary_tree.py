from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        max_width = 0
        queue = deque()
        if root:
            queue.append([root, 1])
            size = len(queue)
            while queue:
                start = 0 # we want to know position of first node within that level
                for k in range(size):
                    node, pos = queue.popleft() 
                    if start == 0:
                        start = pos
                    if node.left:
                        queue.append([node.left, 2 * pos - 1])
                
                    if node.right:
                        queue.append([node.right, 2 * pos])

                max_width = max(max_width, pos - start + 1) 
                size = len(queue)
                
        return max_width
        