from typing import List
from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # lookup to check for possible far jump option 3
        n = len(arr)

        lookup = defaultdict(list)
        for i in range(n):
            lookup[arr[i]].append(i)
    
        # initialize the adjacency list for - NO NEED THIS, we always know its -1, +1 or in the lookup
        # undirected (we can jump to and from any neighbours) graph, G = (V, E)
        # edge = {}
        # for v in range(n):
        #     if v not in edge.keys():
        #         edge[v] = set()
        #     if v - 1 >= 0:
        #         edge[v].add(v-1)
        #     if v + 1 < n:
        #         edge[v].add(v+1)
        #     if len(lookup[arr[v]]) > 1: # not the only index with this value
        #         edge[v] = edge[v].union(
        #             lookup[arr[v]].difference([v]) # remove itself 
        #         )

        # initialize for BFS
        visit = [0 for _ in range(n)]
        queue = deque([])

        queue.append([0, 0]) # index/vertex, num_jump counter
        visit[0] = 1

        while queue:
            v, jump_cnt = queue.popleft()
            if v == n-1:
                return jump_cnt
            # we know anything beyond n-1 is guaranteed to be suboptimal (as good as doing +1 all the way)
            if v-1 >= 0 and visit[v-1] == 0:
                visit[v-1] = 1
                queue.append([v-1, jump_cnt+1])

            if v+1 < n and visit[v+1] == 0:
                visit[v+1] = 1
                queue.append([v+1, jump_cnt+1])
            
            if arr[v] in lookup.keys():
                for nbr in lookup[arr[v]]:
                    if visit[nbr] == 0:
                        visit[nbr] = 1
                        queue.append([nbr, jump_cnt+1])

                del lookup[arr[v]]

sol = Solution()
arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404] # 3 -- OK 
# arr = [7] # 0 -- OK
# arr = [7, 6, 9, 6, 9, 6, 9, 7] # 1 -- OK
# arr = [7, 7, 2, 1, 7, 7, 7, 3, 4, 1] # 3 -- OK
# arr = [68,-94,-44,-18,-1,18,-87,29,-6,-87,-27,37,-57,7,18,68,-59,29,7,53,-27,-59,18,-1,18,-18,-59,-1,-18,-84,-20,7,7,-87,-18,-84,-20,-27]  # TLE
x = sol.minJumps(arr)
print(x)