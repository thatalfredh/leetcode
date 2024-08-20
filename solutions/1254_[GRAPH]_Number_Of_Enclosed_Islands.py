from typing import List
from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        # we can apply BFS or DFS, the number of times we use it (and it valid) = number of closed islands
        # do not count if we led to the borders
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        stack = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    stack.append([i, j])
                    enclosed = 1
                    while stack:
                        r, c = stack.pop()
                        for a, b in directions:
                            nr = r + a
                            nc = c + b
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == 0:
                                    grid[nr][nc] = 1
                                    stack.append([nr,nc])
                            else: # connected to land which is not bounded
                                enclosed = 0
                    count += enclosed
        return count


sol = Solution()
grid = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
res = sol.closedIsland(grid)
        