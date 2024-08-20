from typing import Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Intuition: The problem has simplified due to downward constraint of paths.
        # At each node, one of these can happen:
        # 1. node.val == targetSum
        # 2. node.val + previous node == targetSum
        # 3. (also a case of 2) noide.val + previous sums (of earlier nodes) == targetSum
        count = 0
        stack = deque([[0]])
        def dfs(node, stack, target_sum):
            nonlocal count
            if not node: return 0
            curr_sums = stack[-1]
            new_sums = []
            for s in curr_sums:
                if node.val + s == target_sum: 
                    count += 1
                new_sums.append(node.val + s)
            new_sums.append(0)
            stack.append(new_sums)
            dfs(node.left, stack, target_sum)
            dfs(node.right, stack, target_sum)
            stack.pop() # backtrack
        dfs(root, stack, targetSum)
        return count
        
        ## More efficient with map storing prefix sum
        # count = 0
        # sums = defaultdict()
        # sums[0] = 1
        # def dfs(node, prev_sum):
        #     nonlocal count
        #     if not node: return 0
        #     prev_sum += node.val
        #     count += sums.get(prev_sum - targetSum, 0)
        #     sums[prev_sum] = sums.get(prev_sum, 0) + 1
        #     dfs(node.left, prev_sum)
        #     dfs(node.right, prev_sum)
        #     sums[prev_sum] -= 1 
        # dfs(root, 0)
        # return count

        