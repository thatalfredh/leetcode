from typing import List
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        the answer to this is the same as counting the number of 1s that cannot be reached from the boundary
        """
        
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = deque([])

        for i in [0, m-1]:
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    stack.append([i, j])
                    while stack:
                        r, c = stack.pop()
                        for rd, cd in dirs:
                            nr = r + rd
                            nc = c + cd
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                stack.append([nr, nc])

        for j in [0, n-1]:
            for i in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    stack.append([i, j])
                    while stack:
                        r, c = stack.pop()
                        for rd, cd in dirs:
                            nr = r + rd
                            nc = c + cd
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                stack.append([nr, nc])
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count

sol = Solution()
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
res = sol.numEnclaves(grid)