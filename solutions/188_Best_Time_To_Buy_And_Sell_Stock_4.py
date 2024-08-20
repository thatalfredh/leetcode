from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        f(index, position, k) = {
            Max[
                f(i+1, 1, k) - prices[i], # buy
                f(i+1, 0, k) # do nothing
            ], i = 0
            Max[
                f(i+1, 0, k) + prices[i], # sell
                f(i+1, 1, k) # hold
            ], i = 1
        """
        # n = len(prices)
        # def f(i, position, tx_count):
        #     if i == n or tx_count == k:
        #         return 0
        #     if position == 0:
        #         return max(
        #             -prices[i] + f(i+1, 1, tx_count),
        #             f(i+1, 0, tx_count)
        #         )
        #     else:
        #         return max(
        #             prices[i] + f(i+1, 0, tx_count+1),
        #             f(i+1, 1, tx_count)
        #         )
        # return f(0,0,0)

        # Recursion Tree Pruning by Memoization
        # n = len(prices)
        # memo = [
        #     [
        #         [
        #             -1 for _ in range(k)
        #         ] for _ in range(2)
        #     ] for _ in range(n)
        # ]
        # def f(i, position, tx_count):
        #     if i == n or tx_count == k:
        #         return 0
        #     if memo[i][position][tx_count] != -1:
        #         return memo[i][position][tx_count]
        #     profit = 0
        #     if position == 0:
        #         profit = max(
        #             -prices[i] + f(i+1, 1, tx_count),
        #             f(i+1, 0, tx_count)
        #         )
        #     else:
        #         profit = max(
        #             prices[i] + f(i+1, 0, tx_count+1),
        #             f(i+1, 1, tx_count)
        #         )
        #     memo[i][position][tx_count] = profit
        #     return memo[i][position][tx_count]
        # f(0,0,0)
        # return memo[0][0][0]

        # Optimizing via Tabulation - True DP
        # n = len(prices)
        # dp = [
        #     [
        #         [
        #             0 for _ in range(k+1)
        #         ] for _ in range(2)
        #     ] for _ in range(n+1)
        # ]
        # # the top-down approach in fact starts from index 0, thus 
        # # the bottom-up means we start from n-1
        # for i in range(n-1, -1, -1):
        #     for position in range(2):
        #         for tx_count in range(k):
        #             if position == 0:
        #                 dp[i][position][tx_count] = max(
        #                     -prices[i] + dp[i+1][1][tx_count],
        #                     dp[i+1][0][tx_count]
        #                 )
        #             else:
        #                 dp[i][position][tx_count] = max(
        #                     prices[i] + dp[i+1][0][tx_count+1],
        #                     dp[i+1][1][tx_count]
        #                 )
        # return dp[0][0][0]

        # 4. Space Optimization
        # the key to space optimization is identify how far ahead/back are the results you need to compute the current results
        # so even for 3 dimensional dp, if the update is always only involving dp[i+1][j][k], 
        # all you need is to have 2 separate tables of size (j, k) instead of 1 size(n,j,k)
        n = len(prices)
        curr = [[0 for _ in range(k+1)] for _ in range (2)]
        after = [[0 for _ in range(k+1)] for _ in range (2)]
        for i in range(n-1, -1, -1):
            for position in range(2):
                for tx_count in range(k):
                    if position == 0:
                        curr[position][tx_count] = max(
                            -prices[i] + after[1][tx_count],
                            after[0][tx_count]
                        )
                    else:
                        curr[position][tx_count] = max(
                            prices[i] + after[0][tx_count+1],
                            after[1][tx_count]
                        )
            after = curr
        return after[0][0]
        

        
        