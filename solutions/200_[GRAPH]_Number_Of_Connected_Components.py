from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if visit[i][j] == 0 and grid[i][j] == "1":
                    count += 1
                    visit[i][j] = 1
                    # do BFS
                    queue = deque([])
                    queue.append((i, j))
                    while queue:
                        r, c = queue.popleft()
                        for rd in range(-1, 2):
                            for cd in range(-1, 2):
                                if rd != cd:
                                    nr = r + rd
                                    nc = c + cd
                                    if (
                                        0 <= nr < m and 0<= nc < n and visit[nr][nc] == 0 and grid[nr][nc] == "1"
                                    ):
                                        visit[nr][nc] = 1
                                        queue.append((nr, nc))

        return count
    
sol = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
res = sol.numIslands(grid)
print(res)

print(float("inf") == float("inf"))
                

        