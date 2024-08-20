from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # intuition: since duplicates are not important, we can delete/overwrite them

        l, r = 0, 1
        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            else:
                r += 1
        
        return l + 1

        