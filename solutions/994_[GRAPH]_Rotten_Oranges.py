from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Intuition:
        # It may seem like we can do both BFS or DFS at first, but notice
        # that it may get complicated once we have two rotten oranges at a time
        # thus, BFS will be better
        
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([])
        visit =[[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visit[i][j] = 2
                    queue.append([(i, j), 0])
        minutes = 0
        while queue:
            rc, t = queue.popleft()
            r, c = rc
            for d in dirs:
                rd, cd = d
                nr = r + rd
                nc = c + cd
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    if visit[nr][nc] == 0:
                        visit[nr][nc] = 2
                        minutes = max(minutes, t+1)
                        queue.append([(nr, nc), t+1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visit[i][j] != 2:
                    return -1

        return minutes



        