from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        # Approach 1: We don't seem to make use of the BST property
        lookup = set() # without a lookup, we would be traversing the same path multiple times
        def traverse(node, k):
            if not node:
                return False
            if node.val in lookup:
                return True
            lookup.add(k - node.val)
            l = traverse(node.left, k)
            r = traverse(node.right, k)
            return l or r
        return traverse(root, k)

        # Approach 2: To pre-order traversal to obtain sorted array and apply binary search
        # if not root:
        #     return False
        # arr = []
        # def preorder_traverse(node):
        #     if not node:
        #         return None
        #     preorder_traverse(node.left)
        #     arr.append(node.val)
        #     preorder_traverse(node.right)
        # preorder_traverse(root)
        # def binary_search(l, r, k):
        #     if l > r:
        #         return False
        #     mid = (l + r) // 2
        #     if arr[mid] == k:
        #         return True
        #     elif k < arr[mid]:
        #         return binary_search(l, mid-1, k)
        #     else:
        #         return binary_search(mid+1, r, k)

        # for i in range(len(arr)):
        #     if binary_search(i + 1, len(arr)-1, k - arr[i]):
        #         return True
        # return False
        
        