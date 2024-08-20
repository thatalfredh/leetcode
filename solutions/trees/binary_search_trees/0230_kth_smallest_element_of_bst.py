from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # 2. Better - Only have to traverse K times
        # In-order traversal of BST always results in sorted array 
        # Do up to k times
        cnt = 0
        res = None
        def inorder_traversal(node, k):
            nonlocal cnt, res
            if not node: # count, node value
                return
            inorder_traversal(node.left, k)
            cnt += 1
            if cnt == k:
                res = node.val
            inorder_traversal(node.right, k)
        inorder_traversal(root, k)
        return res
        
        # 1. Brute Force
        # Do In-Order traversal, return result from sorted array
        # vals = []
        # def traverse(node, k):
        #     if not node: return None
        #     traverse(node.left)
        #     vals.append(node.val)
        #     traverse(node.right)
        # traverse(root)
        # if vals:
        #     return vals[k-1]