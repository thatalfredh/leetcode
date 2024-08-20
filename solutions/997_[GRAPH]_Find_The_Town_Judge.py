from typing import List
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # Observation: there exists 1 person which has n-1 trusts AND this person does not contribute to trust
        # people can trust each other

        # TC: 50.26 % | SC: 93.67 %
        # counter = {i: 0 for i in range(1, n+1)}
        # for t in trust:
        #     if t[0] in counter.keys():
        #         counter.pop(t[0])
        #     if t[1] in counter.keys():
        #         counter[t[1]] += 1
        # counter = {v: k for k,v in counter.items()}
        # if n-1 in counter:
        #     return counter[n-1]
        # return -1
        
        # TC: 83.77 % | SC: 93.67 %
        counter = [0 for _ in range(n)]
        for t in trust:
            counter[t[0]-1] = -1
            if counter[t[1]-1] != -1:
                counter[t[1]-1] += 1
        
        for i in range(n):
            if counter[i] == n-1:
                return i+1
        return -1