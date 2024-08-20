from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dirs = [(i, j) for j in range(-1, 2) for i in range(-1, 2)]

        queue = deque([])

        if grid[0][0] == 0:
            queue.append([0, 0, 1])

        while queue:
            i, j, step = queue.popleft()
            
            if i == n-1 and j == n-1:
                return step

            for rd, cd in dirs:
                if rd == 0 and cd == 0: pass
                else:
                    nr = i + rd
                    nc = j + cd
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 1:
                        grid[nr][nc] = 1
                        queue.append([nr, nc, step + 1])
        return -1
    
sol = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
res = sol.shortestPathBinaryMatrix(grid)

print(res)