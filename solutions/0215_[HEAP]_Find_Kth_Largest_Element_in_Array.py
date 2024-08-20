import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # cheese solution - Sorting and Select
        # nums.sort()
        # return nums[-k]

        # # using Heap (Priority Queue)
        # pq = []
        # for n in nums:
        #     heapq.heappush(pq, -n)
        # for _ in range(k):
        #     if _ == k-1:
        #         return -heapq.heappop(pq)
        #     heapq.heappop(pq)

        heapq._heapify_max(nums)
        for _ in range(k):
            if _ == k-1:
                return heapq._heappop_max(nums)
            heapq._heappop_max(nums)

        
    

        