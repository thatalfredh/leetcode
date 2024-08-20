from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        # traverse to each leaf: compute tilt
        # sum up value at node and return to previous call
        tilt = [0]

        def traverse(node):
            if not node: 
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            tilt[0] += abs(left - right)
            return left + right + node.val

        traverse(root)
        return tilt[0]
    
sol = Solution()
# root = [4,2,9,3,5,null,7]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(None)
root.right.right = TreeNode(7)

result = sol.findTilt(root)
