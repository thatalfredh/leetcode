from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # intuition: it can always be added as a leaf
        if not root: 
            return TreeNode(val)
        if root.val > val: # only add to L subtree
            root.left = self.insertIntoBST(root.left, val)
        else: # add to R subtress
            root.right = self.insertIntoBST(root.right, val)
        return root