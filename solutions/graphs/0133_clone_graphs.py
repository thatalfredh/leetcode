# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node:
            g = {}
            queue = deque([])
            g[node.val] = Node(node.val)
            queue.append(node)
            while queue:
                v = queue.popleft()
                for nbr in v.neighbors:
                    if nbr.val not in g:
                        g[nbr.val] = Node(nbr.val)
                        queue.append(nbr)

                    g[v.val].neighbors.append(g[nbr.val])
            return g[node.val]
        