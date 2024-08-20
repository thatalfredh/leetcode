from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Intuition:
        # Be default, top and left edges can flow to Pacific
        # and bottom and right edges can flow to Atlantic.
        # What we want to therefore find is: Which paths can Pacific reach Atlantic and vice versa.
        # We can do two traversals.
        pac, atl = set(), set()

        def dfs(i, j, visited):
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            stack = deque([(i, j)])
            visited.add((i, j))
            while stack:
                r, c = stack.pop()
                for rd, cd in dirs:
                    nr = r + rd
                    nc = c + cd
                    if (
                        0 <= nr < len(heights) and 
                        0 <= nc < len(heights[0]) and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        stack.append([nr, nc])

        for i in range(len(heights)):
            dfs(i, 0, pac)
            dfs(i, len(heights[0])-1, atl)

        for j in range(len(heights[0])):
            dfs(0, j, pac)
            dfs(len(heights)-1, j, atl)

        return pac.intersection(atl)