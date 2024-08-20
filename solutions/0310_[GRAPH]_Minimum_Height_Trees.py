from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # Intuitive Brute Force: DFS every node but 1 <= n <= 2* 10^4; TLE/Mem Exceed
        # Next Intuition:
        # Leaves cannot be the min height tree root (except for n=1)
        # The root of the min height tree "pulls" the "largest mass" of sub trees;
        # the mid point of the longest length of the trees

        def dfs(node, visit):
            """
            return the longest path from given node
            """
            visit[node] = 1
            if len(graph[node]) == 1 and visit[graph[node][0]] == 1:
                return [node]
            else:
                paths = []
                for child in graph[node]:
                    if visit[child] == 0:
                        child_path = dfs(child, visit)
                        paths.append(child_path)
                p = 0
                for i in range(len(paths)):
                    if len(paths[i]) > len(paths[p]):
                        p = i
                # return [node] + max(paths, key=len)
                return [node] + paths[p]

        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        if len(edges) == 0:
            return [0]
        if len(edges) == 1:
            return edges[0]

        stack = deque([])
        max_height = 0
        root = n-1 # arbitrary start
        for i in range(2):
            visit = [0 for _ in range(n)]
            stack.append([root, 0])
            visit[root] = 1
            while stack:
                node, h = stack.pop()
                if h >= max_height:
                    max_height = h
                    start = node
                for child in graph[node]:
                    if visit[child] == 0:
                        stack.append([child, h+1])
                        visit[child] = 1

        visit = [0 for _ in range(n)]
        longest_path = dfs(start, visit)
        # print(longest_path)
        mid = len(longest_path) // 2
        if len(longest_path) % 2 == 1:
            return [longest_path[mid]]
        else:
            return [longest_path[mid-1], longest_path[mid]]

sol = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

mht = sol.findMinHeightTrees(n, edges)
print(mht)