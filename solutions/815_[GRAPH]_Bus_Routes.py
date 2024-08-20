from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # We want to find shortest distance of travel; BFS Traversal
        # any bus within the same route requires 1 bus otherwise +1 for every other route change
        
        n = len(routes)
        graph = defaultdict(list)
        for bus in range(n):
            for stop in routes[bus]:
                graph[stop].extend(
                    set(routes[bus]).difference(set([stop]))
                )
        print(graph)

        visit = set()
        queue = deque([])

        visit.add(source)
        queue.append([source, 0])
       
        
        while queue:
            bus_stop, bus_cnt = queue.popleft()
            print(bus_stop)
            print(graph)

            if bus_stop == target:
                return bus_cnt
            
            if bus_stop in graph.keys():
                for nbr in graph[bus_stop]:
                    if nbr not in visit:
                        visit.add(nbr)
                        queue.append([nbr, bus_cnt+1])
                del graph[bus_stop]
                
        return -1

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source = 15
target = 12
sol = Solution()
res = sol.numBusesToDestination(routes, source, target)
print(res)


        