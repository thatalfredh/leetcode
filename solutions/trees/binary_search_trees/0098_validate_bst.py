from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def traverse_inorder(node, arr):
            if not node: return None
            traverse_inorder(node.left, arr)
            arr.append(node.val)
            traverse_inorder(node.right, arr)
        traverse_inorder(root, arr)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True

        # Iterative Solution
        # stack = deque([])
        # prev = None
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     if prev and root.val <= prev.val:
        #         return False
        #     prev = root
        #     root = root.right
        # return True
