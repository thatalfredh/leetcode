from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distances = [[0 for j in range(n)] for i in range(m)]
        visit = [[0 for j in range(n)] for i in range(m)]
        queue = deque([])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([(i, j), 0])
                    visit[i][j] = 1
                else:
                    visit[i][j] = 0 
        while queue:
            rc, dist = queue.popleft()
            i, j = rc[0], rc[1]
            distances[i][j] = dist
            for d in directions:
                row = i + d[0]
                col = j + d[1]
                if 0 <= row < m and 0 <= col < n:
                    if visit[row][col] == 0:
                        visit[row][col] = 1
                        queue.append([(row, col), dist+1])
        return distances
        


    
sol = Solution()
inp = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

# inp = [
#     [1,0,1,1,0,0,1,0,0,1],
#     [0,1,1,0,1,0,1,0,1,1],
#     [0,0,1,0,1,0,0,1,0,0],
#     [1,0,1,0,1,1,1,1,1,1],
#     [0,1,0,1,1,0,0,0,0,1],
#     [0,0,1,0,1,1,1,0,1,0],
#     [0,1,0,1,0,1,0,0,1,1],
#     [1,0,0,0,1,1,1,1,0,1],
#     [1,1,1,1,1,1,1,0,1,0],
#     [1,1,1,1,0,1,0,0,1,1]
#  ]
sol.updateMatrix(inp)