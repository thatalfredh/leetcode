from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def find_min(self, root):
        if not root.left: 
            return root
        return self.find_min(root.left)
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Intuition:
        # We need to ensure the property of BST is preserved.
        # That is, L < Root < R. Then, given key, we also know which subtree to search.
        # If key < root, we modify left subtress. If key > root, modify right subtree.
        # Some cases for deletion:
        # 1. isLeaf - delete
        # 2. hasChild - set reference to child before deletion
        # 3. hasChildren - the smallest descendent larger than the root to be deleted can become new root

        """
        Example 2:
                    5
            3              6
        2       4              7
                                    8
        """
        if not root: return None
        if root.val == key:
            if not root.left and not root.right: # isLeaf
                return None
            elif not root.left: # hasChild
                return root.right
            elif not root.right: # hasChild
                return root.left
            else: # hasChildren
                # find the smallest descendent on right subtree
                # set the reference to this node
                min_node = self.find_min(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
        
        