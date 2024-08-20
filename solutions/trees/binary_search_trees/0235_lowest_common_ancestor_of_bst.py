from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Intuition: Given a BST and nodes p and q, they fall into one of the cases:
        # p and q < root.val OR p and q > root.val; same subtree
        # p < root.val and q > root.val OR p > root.val and q < root.val; difference subtree

        # Approach 1: Recursion
        # if root == p or root == q or (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
        #     return root
        # if p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return root
        # Approach 2: Iterative
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
        return root
                

        

        