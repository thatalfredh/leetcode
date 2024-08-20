from typing import List
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Logic: If a course has a pre-requisite which also a requisite of another course to be completed underway,
        # we will not be able to complete all courses
        # V --> W --> X --> Y --> Z ; must do z to do y ... to do V
        # but now Z --> V or any others e.g. Z --> X
        # must complete X to do Z but X depends on Y which depends on Z; impossible

        graph = defaultdict(list)
        prereq_cnt = [0 for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0]) # b is the prequisite for [a1, a2,..]
            prereq_cnt[prerequisites[i][0]] += 1

        stack = deque([])
        tsort = []

        for i in range(numCourses):
            if prereq_cnt[i] == 0:
                tsort.append(i)
                stack.append(i)
                
        while stack:
            course = stack.pop()
            for i in graph[course]:
                prereq_cnt[i] -= 1
                if prereq_cnt[i] == 0:
                    stack.append(i)
                    tsort.append(i)

        return sum(prereq_cnt) == 0