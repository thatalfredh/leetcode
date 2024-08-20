from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Intuition: 
        A province is created by group of cities that can be travelled from one to another.
        The number of times we do a new DFS on an unvisited city is the number of provinces.
        """
        visit = [0 for _ in range(len(isConnected))]
        count = 0
        stack = deque([])
        for i in range(len(visit)):
            if visit[i] == 0:
                visit[i] = 1
                # DFS
                stack.append(i)
                while stack:
                    i = stack.pop()
                    for j in range(len(isConnected)):
                        if isConnected[i][j] and visit[j] == 0:
                            visit[j] = 1
                            stack.append(j)
                count += 1
        return count