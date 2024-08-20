from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Intuition:
        # Given the bounds, we can trim the tree at every node using the BST property
        # Once a node.val is below the lower bound, we trim always this node along with it's left subtree, return the right subtree.
        # Conversely, return the left subtree once node.val exceed the upper bound
        if not root: return None
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val < low:
            root = root.right
        elif root.val > high:
            root = root.left
        return root