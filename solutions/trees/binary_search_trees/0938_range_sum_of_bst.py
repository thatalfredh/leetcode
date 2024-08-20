from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # BST: We can traverse until L = Low
        # def range_sum(node, low, high):
        #     if not node: return 0
        #     if low <= node.val <= high:
        #         left = range_sum(node.left, low, high)
        #         right = range_sum(node.right, low, high)
        #         return left + right + node.val
        #     if node.val < low:
        #         return range_sum(node.right, low, high)
        #     if node.val > high:
        #         return range_sum(node.left, low, high)
        #     return range_sum_2(root, low, high)
        def range_sum_2(node, low, high):
            if not node: return 0
            left = range_sum_2(node.left, low, high)
            right = range_sum_2(node.right, low, high)
            if low <= node.val <= high:
                return left + right + node.val
            else:
                return left + right

        return range_sum_2(root, low, high)