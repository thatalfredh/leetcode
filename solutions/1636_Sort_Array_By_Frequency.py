from collections import defaultdict
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums 
        nums.sort()
        counter = defaultdict(list)
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                counter[cnt].append(nums[i-1])
                cnt = 1
                if i == len(nums)-1:
                    counter[1].append(nums[i])
            else:
                cnt += 1
                if i == len(nums)-1:
                    counter[cnt].append(nums[i])

        res = []
        for k in sorted(counter.keys()):
            for v in counter[k][::-1]:
                res.extend([v] * k)

        return res
            

        