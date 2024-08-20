from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # intuition: similar to the version 1 of this problem, 
        # we can still employ the two pointers technique but
        # this time the way we check for deletion is different

        # l = 0
        # r = 0
        # while r < len(nums):
        #     cnt = 1
        #     while r + 1 < len(nums) and nums[r] == nums[r+1]:
        #         cnt += 1
        #         r += 1
        #     for i in range(min(cnt, 2)):
        #         nums[l] = nums[r]
        #         l += 1
        #     r += 1
        # return l

        l = 1
        r = 1
        cnt = 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l