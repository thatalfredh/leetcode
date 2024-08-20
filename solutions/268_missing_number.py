from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # most intuitive - sort array O(nlogn) and traverse O(1)
        # faster - add into set, enumerate through it O(n) but using additional space of O(n)
        # even more efficient - using XOR, basic arithmetic sum, paired elimination
        
        # XOR: n ^ k ^ n = (n ^ n) ^ k = 0 ^ k = k
        # n = len(nums)
        # res = n
        # for i in range(n):
        #     res ^= i^nums[i]
        # return res

        # paired elimination
        n = len(nums)
        res = n
        for i in range(n):
            res += (i - nums[i])
        return res