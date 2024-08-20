from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Brute Force (Recursion): explore all possible ways to climb the stairs (including cost)
        # i.e. number steps * cost
        # def f(i):
        #     # base case
        #     if i > len(cost) - 1:
        #         return 0
        #     if i < 0:
        #         return min(f(i+1), f(i+2))
        #     else:
        #         return cost[i] + min(f(i+1), f(i+2))
        # return f(-1)
        
        # Recursion Tree Pruning by Memoization: 
        # an visualize recursion by a tree (effectively a DFS)
        # can memoize to avoid recomputing branches
        # dp = [-1] * len(cost)
        # def f(i):
        #     # base case
        #     print(i, dp)
        #     if i > len(cost) - 1:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     if i < 0:
        #         return min(f(i+1), f(i+2))
        #     # else:
        #     #     return cost[i] + min(f(i+1), f(i+2))
        #     dp[i] = cost[i] + min(f(i+1), f(i+2))
        #     return dp[i]
        # f(-1)
        # print(dp)
        # return min(dp[-2], dp[-1])

        # tabulation - True DP
        # if we use the minimum cost to reach each step prior, we are certain 
        # to reach the top using the global minimum cost
        dp = [-1] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-2], dp[-1])
            


        