from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # Intuition: BFS, store path in queue
        paths = []
        queue = deque([])
        if root:
            queue.append([root, str(root.val)])
            size = len(queue)
            while queue:
                for _ in range(size):
                    node, path = queue.popleft()
                    if not node.left and not node.right:
                        paths.append(path)
                    if node.left:
                        queue.append([node.left, f"{path}->{node.left.val}"])
                    if node.right:
                        queue.append([node.right, f"{path}->{node.right.val}"])
                size = len(queue)
        return paths

        # Recursive
        paths = []
        def dfs(node, path, result):
            if not node:
                return None
            path = f"{path}->{node.val}" if path else str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                dfs(node.left, path, result)
                dfs(node.right, path, result)
        dfs(root, "", paths)
        return paths

        

        