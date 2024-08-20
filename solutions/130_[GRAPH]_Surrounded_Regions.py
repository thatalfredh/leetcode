from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # intuition: for a cell (or one that of the region)to be bounded in one, 
        # all connected O must lead to boundary X

        # idea: DFS all four directions, the return value after encountering 
        # the boundary should inform us of validity of region
        m = len(board)
        n = len(board[0])
        visit = [
            [
                0 for _ in range(n)
            ] for _ in range(m)
        ]
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        def dfs(i, j):
            visit[i][j] = 1
            for d in directions:
                row, col = i + d[0], j + d[1]
                if 0 <= row < m and 0 <= col < n:
                    if visit[row][col] != 1 and board[row][col] == "O":
                        dfs(row, col)
            
        for i in [0, m-1]:
           for j in range(n):
               if board[i][j] == "O":
                   dfs(i, j)
        
        for j in [0, n-1]:
            for i in range(m):
                if board[i][j] == "O":
                   dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if visit[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"
        print(board)

sol = Solution()
inp = [
    ["O","X","X","O","X"],
    ["X","O","O","X","O"],
    ["X","O","X","O","X"],
    ["O","X","O","O","O"],
    ["X","X","O","X","O"]
]
sol.solve(inp)

        
        