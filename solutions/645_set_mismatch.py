from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # intuitive: iterate the array O(n), add each element to HashSet O(n) space
        # duplicate is found when element already exists, enumerate the HashSet to find missing value O(n)

        # [1,2,3,4]: XOR every index value pair = 0
        
        dup = -1
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0: # this number has been encountered before
                dup = abs(nums[i])
            else: nums[idx] *= -1
        # [1, 2, 2, 4] ---> [-1, -2, 2, -4] 
        # this means that index 2 was not visited because there was no value 3 in the array
        # rmb that the values are from 1 to n, thus minus 1 to convert into index
        mis = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                mis = i + 1

        return [dup, mis]

        
        
        
        