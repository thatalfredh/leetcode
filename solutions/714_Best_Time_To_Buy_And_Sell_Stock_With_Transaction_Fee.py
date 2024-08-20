from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [
            [
                0 for _ in range(2)
            ] for _ in range(2)
        ]
        for i in range(n-1, -1, -1):
            dp[0][0] = max(
                -prices[i] + dp[1][1],
                dp[1][0]
            )
            dp[0][1] = max(
                prices[i] + dp[1][0] - fee,
                dp[1][1]
            )
            dp[1] = dp[0][:]
        return dp[0][0]