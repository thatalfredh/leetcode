from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            # both NULL
            if not p and not q:
                return True
            # one is NULL
            if p and not q:
                return False
            # both not NULL - need to check as node can take diff value
            if p and q:
                return (p.val == q.val) and check(p.left, q.right) and check(p.right, q.left)

        if root:
            return check(root.left, root.right)
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(None)
root.right.left = TreeNode(None)
root.right.right = TreeNode(3)

sol = Solution()
result = sol.isSymmetric(root)
print(result)