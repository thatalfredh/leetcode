from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]: # positive return, take profit
        #         profit += (prices[i] - prices[i-1])

        # return profit

        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
        return profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))