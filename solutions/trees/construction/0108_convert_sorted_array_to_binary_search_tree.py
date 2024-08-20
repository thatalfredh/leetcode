from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # to keep it balance, we can keep taking the middle value as the node value
        def height_balance(i, j):
            if j >= i:
                mid = (i+j) // 2
                node = TreeNode(nums[mid])
                node.left = height_balance(i, mid-1)
                node.right = height_balance(mid+1, j)
                return node

        n = len(nums)
        root = None
        if n:
            root = height_balance(0, n-1)
        return root
        
