from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        visit = [0 for _ in range(n)]

        def dfs(i):
            if visit[i] == 1:
                return
            visit[i] = 1
            for k in rooms[i]:
                dfs(k)
        dfs(0)
        return sum(visit) == n

sol = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
res = sol.canVisitAllRooms(rooms)
print(res)