from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # prereq_cnt[i] is the number of prereq courses for course i
        prereq_cnt = [0 for _ in range(numCourses)]

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            prereq_cnt[prereq[0]] += 1
        print(prereq_cnt)

        tsort = []
        stack = deque([])
        for i in range(numCourses):
            if prereq_cnt[i] == 0:
                tsort.append(i)
                stack.append(i)
        print(stack)

        while stack:
            c = stack.pop()
            for dep in graph[c]:
                prereq_cnt[dep] -= 1
                if prereq_cnt[dep] == 0:
                    tsort.append(dep)
                    stack.append(dep)
        print(prereq_cnt)
        return tsort if sum(prereq_cnt) == 0 else []