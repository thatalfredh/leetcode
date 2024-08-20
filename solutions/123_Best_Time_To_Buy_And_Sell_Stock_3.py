from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # # 1. Recursive Logic Approach
        # # note: prices here can take 0 value, so need a flag to indicate position instead of price
        # # also since there is constraint of at most 2 transaction, we can return when count = 2
        # n = len(prices)
        # def f(i, position, tx_count):
        #     if i == n or tx_count == 2:
        #         return 0
        #     if position == 0: # Can Buy / Skip
        #         return max(
        #             -prices[i] + f(i+1, 1, tx_count), # Buy
        #             f(i+1, 0, tx_count) # Skip
        #         )
        #     else: # Can Sell / Skip
        #         return max(
        #             prices[i] + f(i+1, 0, tx_count+1), # Sell
        #             f(i+1, 1, tx_count), # Hold
        #         )
        # return f(0, 0, 0)

        # # 2. Top Down with Memoization - prunes the recursion tree
        # # From the Recursion Tree, we indentified number of variables (3)
        # # index (n), position (2), transaction (3); size(memo) = n * 2 * 3
        # # num transactions x position x timestep
        # n = len(prices)
        # # memo = [[[-1] * 3] * 2 ] * n # tracks the max profit for each given action
        # memo = [
        #     [
        #         [
        #             -1 for _ in range(3)
        #         ] for _ in range(2)
        #     ] for _ in range(n)
        # ]
        # def f(i, position, tx_count, memo):
        #     if i == n or tx_count == 2:
        #         return 0
        #     if memo[i][position][tx_count] != -1:
        #         return memo[i][position][tx_count]

        #     profit = 0
        #     if position == 0: # Can Buy / Skip
        #         profit = max(
        #             -prices[i] + f(i + 1, 1, tx_count, memo), # Buy
        #             f(i + 1, 0, tx_count, memo) # Skip
        #         )
        #     else: # Can Sell / Skip
        #         profit = max(
        #             prices[i] + f(i + 1, 0, tx_count + 1, memo), # Sell
        #             f(i + 1, 1, tx_count, memo) # Hold
        #         )
        #     memo[i][position][tx_count] = profit
        #     return profit

        # f(0, 0, 0, memo)
        # return memo[0][0][0]

        # 3. Tabulation - True DP
        # a. base cases; convert from recursive solution (i.e. "if idx == 0: return 0" means
        # that position and tx_count can take any value)
        # b. identify changing params (i.e. 3 in 3D DP); 3 nested loops
        # for loops, if recursive solution started from 0, then dp starts from n-1, otherwise is true
        # c. copy recurrence
        n = len(prices)
        dp = [
            [
                [
                    0 for _ in range(3+1)
                ] for _ in range(2)
            ] for _ in range(n + 1)
        ]
        for i in range(n-1, -1, -1):
            for position in range(2):
                for tx_count in range(2):
                    # print(i)
                    if position == 0: # can buy / skip
                        dp[i][position][tx_count] = max(
                            -prices[i] + dp[i+1][1][tx_count], # buy
                            dp[i+1][0][tx_count] # skip
                        )
                    else: # can sell / skip
                        dp[i][position][tx_count] = max(
                            prices[i] + dp[i+1][0][tx_count+1], # sell
                            dp[i+1][1][tx_count] # hold
                        )
        print(dp)
        return dp[0][0][0]



    
sol = Solution()
# inp = [1, 5, 2, 4] # 6 - OK
# inp = [7, 1, 5, 3, 6, 4] # 7 - OK
inp = [3, 3, 5, 0, 0, 3, 1, 4] # 6 - OK
# inp = [1, 2, 3, 4, 5] # 4 - OK
# inp = [7, 6, 4, 3, 1] # 0 - OK
print(sol.maxProfit(inp))

# print(sol.maxProfit(inp)[0][0][0])