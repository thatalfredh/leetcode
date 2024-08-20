"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List
from collections import defaultdict, deque

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
        
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        lookup = defaultdict(dict)
        # lookup = defaultdict()
        """
        {
            '1':{
                'imp': 5,
                'subs': [2, 3]
            },
            '2':{
                'imp': 3,
                'subs': []
            }
            .
            .
        }
        """
        for i in range(len(employees)):
            lookup[employees[i].id]['imp'] = employees[i].importance
            lookup[employees[i].id]['subs'] = employees[i].subordinates
            # lookup[employees[i].id] = employees[i]
        
        total_imp = 0
        stack = deque([])

        stack.append(id)
        while stack:
            id = stack.pop()
            total_imp += lookup[id]['imp']
            for s in lookup[id]['subs']:
               stack.append(s)
            # total_imp += lookup[id].importance
            # stack.extend(lookup[id].subordinates)

        return total_imp