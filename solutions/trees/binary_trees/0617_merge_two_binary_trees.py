from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # # !p and q / p and !q
        # if root1 and not root2:
        #     return root1

        # if not root1 and root2:
        #     return root2

        # # p and q both NULL
        # if not root1 and not root2:
        #     return root1

        # # p and q both NOT NULL
        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)

        # return root1

        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
    

sol = Solution()
# root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.left = TreeNode(None)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(None)
root2.right.right = TreeNode(7)

root1 = sol.mergeTrees(root1, root2)