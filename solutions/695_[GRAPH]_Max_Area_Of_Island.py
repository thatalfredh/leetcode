from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Intuition:
        - At each cell 1, we do a DFS until termination, mark as visit along the way
        (can either use visit matrix or do in-place)
        """
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        max_area = 0
        stack = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 1
                    grid[i][j] = 0
                    stack.append([i, j])
                    while stack:
                        r, c = stack.pop()
                        for rd, cd in dirs:
                            nr = r + rd
                            nc = c + cd
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                area += 1
                                grid[nr][nc] = 0
                                stack.append([nr, nc])
                    max_area = max(max_area, area)

        return max_area

sol = Solution()                    
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
res = sol.maxAreaOfIsland(grid)

print(res)

        