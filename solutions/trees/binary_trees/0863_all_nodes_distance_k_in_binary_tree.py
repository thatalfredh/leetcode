from typing import List
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # slow but intuitive way to do this would be in two phases:
        # build graph from BFS traversal of the tree
        # BFS traversal the graph

        # BUT HOW TO DO THIS IN RECURSION??
        values = []
        
        def traverse(node):
            if node.left:
                lookup[node.left] = node
                traverse(node.left)
            if node.right:
                lookup[node.right] = node
                traverse(node.right)
        if root:
            lookup = defaultdict()
            traverse(root)

            queue = deque()
            visit = set()

            queue.append(target)
            visit.add(target)

            while queue and k > 0:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()

                    if node in lookup:
                        if lookup[node] not in visit:
                            visit.add(lookup[node])
                            queue.append(lookup[node])

                    if node.left and node.left not in visit:
                        visit.add(node.left)
                        queue.append(node.left)

                    if node.right and node.right not in visit:
                        visit.add(node.right)
                        queue.append(node.right)
                k -= 1
            while queue:
                values.append(queue.popleft().val)

        return values

# [3,5,1,6,2,0,8,null,null,7,4]    
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()
result = sol.distanceK(root, root.left, 2)

print(result)


                
             
                

        

        