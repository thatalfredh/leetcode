from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Minimum Absolute difference can be obtained by two values near to each other
        # Do preorder traversal, compute diff with previous value each time
        # Optimal Solution - WHY?
        # def traverse(node, x1, x2):
        #     if not node:
        #         return abs(x2-x1)
        #     left = traverse(node.left, x1, node.val)
        #     right = traverse(node.right, node.val, x2)
        #     return min(left, right)
        # return traverse(root, float("-inf"), float("inf"))
        prev = [None]
        mad = [float("inf")]
        def traverse(node):
            if not node:
                return None
            left = traverse(node.left)
            if prev[0] is not None:
                mad[0] = min(mad[0], abs(prev[0] - node.val))
            prev[0] = node.val
            right = traverse(node.right)
        traverse(root)
        return mad[0]