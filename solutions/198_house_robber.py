from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

       # at each index, we either rob or not rob
       # if rob, we must skip the next
       # if not rob, we can rob or skip the next
       
       # recursive approach
    #    n = len(nums)
    #    dp = [0] * n
    #    def f(i, nums, dp):
    #         if i == 0: return nums[i]
    #         if i < 0: return 0
    #         if dp[i] != 0: return dp[i]
    #         dp[i] = max(
    #             nums[i] + f(i-2, nums, dp), # rob
    #             0 + f(i-1, nums, dp), # not rob
    #         )
    #         return dp[i]

    #    return f(n-1, nums, dp)

        # # tabulation approach
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     a = nums[i] + (dp[i-2] if i > 1 else 0)
        #     b = 0 + dp[i-1]
        #     dp[i] = max(a, b)

        # return dp[-1]

        # space optimized
        n = len(nums)
        dp = [0, 0]
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            a = nums[i] + (dp[0] if i > 1 else 0)
            b = 0 + dp[1]
            dp[0] = dp[1]
            dp[1] = max(a, b)
        return dp[1]