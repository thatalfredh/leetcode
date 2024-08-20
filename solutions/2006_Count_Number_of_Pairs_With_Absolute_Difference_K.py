from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # just need the count of pairs
        # then if, there are one 1 and five 2, we will have 1 * 5 pairs
        count = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] not in count.keys():
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
                
        for j in count.keys():
            if j + k in count.keys():
                res += count[j + k] * count[j]
        return res
                

        