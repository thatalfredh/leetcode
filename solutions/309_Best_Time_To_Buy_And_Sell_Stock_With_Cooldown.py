from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # intuition: with the cooldown, greedily approach will not work
        # why: [2, 7, 1, 7]
        # Intuitive Solution: Recursive
        # n = len(prices)
        # def f(i, position):
        #     if i >= n: 
        #         return 0
        #     if position == 0: # can buy
        #         return max(
        #             -prices[i] + f(i+1, 1),
        #             f(i+1, 0)
        #         )
        #     else: # long position, can only sell
        #         return max(
        #             prices[i] + f(i+2, 0),
        #             f(i+1, 1)
        #         )
        # return f(0, 0)

        # # Improved Solution: Memoized
        # n = len(prices)
        # memo = [
        #     [
        #         -1 for _ in range(2)
        #     ] for _ in range(n)
        # ]
        # def f(i, position, memo):
        #     if i >= n: 
        #         return 0
        #     if memo[i][position] != -1:
        #         return memo[i][position]
        #     profit = 0
        #     if position == 0: # can buy
        #         profit = max(
        #             -prices[i] + f(i+1, 1, memo), # buy
        #             f(i+1, 0, memo) # do nothing
        #         )
        #     else: # long position, can only sell
        #         profit =  max(
        #             prices[i] + f(i+2, 0, memo), # sell
        #             f(i+1, 1, memo) # hold
        #         )
        #     print(memo)
        #     memo[i][position] = profit
        #     return profit
        # f(0, 0, memo)
        # return memo[0][0]

        # Tabulation
        # n = len(prices)
        # dp = [
        #     [
        #         0 for i in range(2)
        #     ] for _ in range(n+2)
        # ]
        # for i in range(n-1, -1, -1):
        #     for position in range(2):
        #         if position == 0:
        #             dp[i][position] = max(
        #                 -prices[i] + dp[i+1][1],
        #                 dp[i+1][0]
        #             )
        #         else:
        #             dp[i][position] = max(
        #                 prices[i] + dp[i+2][0],
        #                 dp[i+1][1]
        #             )
        #     print(dp)
        # return dp[0][0]

        # # Space Optimized
        n = len(prices)
        dp = [
            [
                0 for i in range(2)
            ] for _ in range(3)
        ]
        for i in range(n-1, -1, -1):
            dp[0][0] = max(
                -prices[i] + dp[1][1],
                dp[1][0]
            )
            dp[0][1] = max(
                prices[i] + dp[2][0],
                dp[1][1]
            )
            dp[2] = dp[1][:] # need to do use slice to create new list; avoid duplicating reference
            dp[1] = dp[0][:]

        return dp[0][0]
    
sol = Solution()
inp = [1,2,3,4,2,7,1,7]
print(sol.maxProfit(inp))










        