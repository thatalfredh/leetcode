from typing import List
from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # DFS graph: manager -> subordinates 
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)

        # minutes = [float("inf") for _ in range(n)]
        # minutes[headID] = 0 
        # the time needed to inform all the employees is lower bounded by the longest path
        stack = deque([])
        stack.append([headID, informTime[headID]])
        minutes = 0
        while stack:
            emp, t = stack.pop()
            minutes = max(minutes, t)
            for sub in graph[emp]:
                # minutes[sub] = t
                if sub in graph and graph[sub]:
                    stack.append([sub, t + informTime[sub]])

        return minutes    