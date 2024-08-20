from typing import List
from collections import defaultdict, deque

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        lookup = defaultdict(dict)
        for e in edges:
            lookup[e[0]][e[1]] = e[2]
            lookup[e[1]][e[0]] = e[2]

        queue = deque([])
        # counter = defaultdict(list)
        ans = -1
        min_count = float("inf")

        for i in range(n):

            count = 0
            visit = [float("inf")] * n
            visit[i] = 0
            queue.append([i, 0])
            
            while queue:
                city, dist = queue.popleft()

                if city in lookup.keys():
                    for to in lookup[city]:
                        d = dist + lookup[city][to]
                        if d <= distanceThreshold:
                            if visit[to] == float("inf"):
                                count += 1

                            if d <= visit[to]:
                                visit[to] = d
                                queue.append([to, d])
            if count <= min_count:
                min_count = count
                ans = max(ans, i)

        return ans
        
            # counter[count].append(i)
        # return max(counter[min(counter.keys())]