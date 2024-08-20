import heapq
from typing import List

class Solution:
    # def maxEvents(self, events: List[List[int]]) -> int:
    #     n = len(events)
    #     # Sort by startDay(needed), endDay (minimizes number of swaps when pushing in heap)
    #     events.sort()

    #     # Min-heap that stores endDay for started events
    #     started = []
    #     count = i = 0
    #     # First day an event starts
    #     curr_day = events[0][0]
    #     # While some event hasn't been added to heap
    #     while i<n:
    #         # Add all events that start on curr_day
    #         while i<n and events[i][0]==curr_day:
    #             heappush(started, events[i][1])
    #             i += 1

    #         # Attend started event that ends earliest
    #         heappop(started)
    #         count += 1
    #         curr_day += 1
            
    #         # Remove all expired events
    #         while started and started[0]<curr_day: heappop(started)
    #         # If no started events left, move to the next startDay
    #         if i<n and not started: curr_day = events[i][0]

    #     # Events that started that are still left in heap
    #     while started:
    #         # Non-expired started event that ends earliest
    #         if heappop(started)>=curr_day:
    #             curr_day += 1
    #             count += 1
    #     return count

    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort()
        pq = [] # priority queue: the top is the event with earliest ending time
        idx = 0
        res = 0
        
        day = events[0][0]
        while idx < len(events):
            # add all events starting on a given day
            while idx < len(events) and events[idx][0] == day:
                heapq.heappush(pq, events[idx][1])
                idx += 1
            # attend an event
            if pq:
                heapq.heappop(pq)
                res += 1
                day += 1
            # remove events that can no longer be attended
            while pq and pq[0] < day:
                heapq.heappop(pq)

            # if there is gap between events starting - slack time
            if not pq and idx <len(events):
                day = events[idx][0]

        while pq:
            if heapq.heappop(pq) >= day:
                day += 1
                res += 1

        return res