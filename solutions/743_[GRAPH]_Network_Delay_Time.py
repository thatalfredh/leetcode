from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Intuition: edge represents distance (time taken), BFS can be applied
        # source --> map (dest, time)
        # {
        #     2: {
        #         2: 1,
        #         3, 1
        #     }
        #     3: {
        #         4: 1
        #     }
        # }
        # the minimum time for all n nodes to receive depends on the fartherst node max(shortest time of each nodes)
        lookup = defaultdict(dict)
        for i in range(len(times)):
            lookup[times[i][0]][times[i][1]] = times[i][2]
        
        visit = [float("inf")] * n
        queue = deque([])
        queue.append([k, 0])
        visit[k-1] = 0 

        while queue:
            node, t = queue.popleft()

            if t > visit[node-1]:
                continue

            if node in lookup.keys():
                for nbr, t_nbr in lookup[node].items():
                    curr_time = t + t_nbr
                    # if the new time for signal to reach this node is worse, 
                    # it also means subsequent propagation will be worse
                    if curr_time < visit[nbr-1]: 
                        visit[nbr-1] = curr_time
                        queue.append([nbr, curr_time])

        res = max(visit)
        return res if res < float("inf") else -1