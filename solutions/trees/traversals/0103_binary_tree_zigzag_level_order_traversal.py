from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        if root:
            flag = 1
            queue = deque([])
            queue.append(root)
            while queue:
                size = len(queue)
                level = []
                for _ in range(size):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

                if flag == 1:
                    values.append(level)
                else:
                    values.append(level[::-1])
                    
                flag *= -1

        return values
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.zigzagLevelOrder(root)
print(result)  