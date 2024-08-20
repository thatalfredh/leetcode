from typing import List
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        costs = defaultdict(dict)
        for i in range(len(flights)): # O(M) where M is the number of flights
            costs[flights[i][0]][flights[i][1]] = flights[i][2]
        
        """
        {
            city_0: {
                city_1: cost_01
            },
            city_1: {
                city_2: cost_12,
                city_3: cost_13
            }
        }
        """
        visit = [float("inf") for _ in range(n)]
        queue = deque([])
        visit[src] = 0
        queue.append([src, -1, 0]) # city, stops, cost
        # with the parameter k, we do not want the shortest path
        # that means we should traverse up till k times and return the lowest cost
        # that means we should also not return as soon as we encounter stops > k for this implmentation
        while queue:
            #print(queue)
            city, stops, cost = queue.popleft()
            if stops > k:
                continue
            # if city == dst:
            #     res = min(res, cost)
            if city in costs.keys():
                for destination, price in costs[city].items():
                    if visit[destination] > cost + price and stops < k:
                        visit[destination] = cost + price
                        queue.append([destination, stops+1, cost + price])

        return -1 if visit[dst] == float("inf") else visit[dst]



# flights = [[0,1,100],[1,2,100],[0,2,500]]
# n = 3
# src = 0
# dst = 2
# k = 1

flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
n = 4
src = 0 
dst =  3
k = 1

# flights = [[3,0,8],[1,4,1],[1,0,4],[1,3,3],[3,4,1],[2,3,3],[2,0,10]]
# n = 5
# src = 1
# dst = 4
# k = 1

sol = Solution()
res = sol.findCheapestPrice(n, flights, src, dst, k)

print(res)
