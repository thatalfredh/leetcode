from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        paths = []
        stack = deque([])
        def dfs(node, remainder):
            if not node: 
                return
            remainder -= node.val
            stack.append(node.val)
            if not node.left and not node.right and remainder == 0:
                paths.append(list(stack))
            if node.left:
                dfs(node.left, remainder)
            if node.right:
                dfs(node.right, remainder)
            stack.pop() # backtracking

        dfs(root, targetSum)
        return paths

        # def dfs(node, path, target_sum, paths):
        #     if not node: return
        #     curr_sum = target_sum - node.val
        #     curr_path = path + [node.val]

        #     if not node.left and not node.right and curr_sum == 0:
        #         paths.append(curr_path)
        #     else:
        #         dfs(node.left, curr_path, curr_sum, paths)
        #         dfs(node.right, curr_path, curr_sum, paths)

        # dfs(root, [], targetSum, paths)
        # return paths

        # if root:
        #     queue = deque([])
        #     queue.append([root, [root.val]])
        #     size = len(queue)
        #     while queue:
        #         for _ in range(size):
        #             node, p = queue.popleft()
        #             if not node.left and not node.right and sum(p) == targetSum:
        #                 paths.append(p)
        #             if node.left:
        #                 queue.append([node.left, p + [node.left.val]])
        #             if node.right:
        #                 queue.append([node.right, p + [node.right.val]])
        #         size = len(queue)

        # return paths

        