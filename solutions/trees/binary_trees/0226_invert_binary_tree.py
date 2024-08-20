from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root:
        #     root.left, root.right = root.right, root.left
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return root
        if root:
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root

#  root = [4,2,7,1,3,6,9]
sol = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

result = sol.invertTree(root)
# print(result)