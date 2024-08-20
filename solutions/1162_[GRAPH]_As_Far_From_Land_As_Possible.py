from typing import List
from collections import deque
class Solution:

    def distance(self, x0, y0, x1, y1):
        return abs(x0-x1) + abs(y0-y1)

    def maxDistance(self, grid: List[List[int]]) -> int:
        
        # Computing a sum or average distace for each water cell will result in same values
        # which is no indicative
        # Intuition: For each land cell, do a BFS and mark the lower of distance at each water cell every iteration
        """
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]

        imagine doing BFS from each land the given grid (cannot)
        imagine doing BFS from each water
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]
        """
        n = len(grid)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i,j, 0])
        max_dist = 0
        while queue:
            i, j, dist = queue.popleft()
            max_dist = max(max_dist, dist)
            for rd, cd in dirs:
                nr = i + rd
                nc = j + cd
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    d = self.distance(i, j, nr, nc)
                    queue.append([nr, nc, dist+1])
            
        return max_dist if max_dist > 0 else -1
                    
        # queue = deque([])
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             # do BFS
        #             visit = [c[:] for c in grid]
        #             queue.append([i, j])
        #             while queue:
        #                 r, c = queue.popleft()
        #                 for d in dirs:
        #                     nr = r + d[0]
        #                     nc = c + d[1]
        #                     if 0 <= nr < n and 0 <= nc < n and visit[nr][nc] == 0:
        #                         visit[nr][nc] = 1
        #                         queue.append([nr, nc])
        #                         d = self.distance(i, j, nr, nc)
        #                         dist[nr][nc] = min(dist[nr][nc], d)
        # res = 0
        # for i in range(n):
        #     for j in range(n):
        #         if dist[i][j] != float("inf"):
        #             res = max(res, dist[i][j])
                    
        # return res if res > 0 else -1