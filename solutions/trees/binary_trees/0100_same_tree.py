from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):

            if not p and not q:
                return True

            if p and not q:
                return False
            
            if p and q:
                v = p.val == q.val
                l = check(p.left, q.left)
                r = check(p.right, q.right)
                return v and l and r
           
        return check(p,q)
        