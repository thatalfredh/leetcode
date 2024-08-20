from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        lookup = defaultdict(dict)
        for i in range(len(equations)):
            lookup[equations[i][0]][equations[i][1]] = values[i]
            lookup[equations[i][1]][equations[i][0]] = 1 / values[i]

        res = []
        stack = deque([])
        for q in queries:  
            if q[0] not in lookup.keys() or q[1] not in lookup.keys():
                res.append(-1.0)
            else:
                ans = -1
                stack.append([q[0], 1])
                visit = set([q[0]])
                while stack:
                    b, r = stack.pop()
                    if b == q[1]:
                        ans = r
                        stack.clear()
                    else:
                        for var in lookup[b].keys():
                            if var not in visit:
                                visit.add(var)
                                stack.append([var, r * lookup[b][var]])
                res.append(ans)

        return res