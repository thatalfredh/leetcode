class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)
        dp = [
            [
                -1 for _ in range(n)
            ] for _ in range(m)
        ]
        def f(i, j, s1, s2, dp):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s1[i] == s2[j]:
                dp[i][j] = 1 + f(i-1, j-1, s1, s2, dp)
            else:
                dp[i][j] = max(
                    f(i-1, j, s1, s2, dp), 
                    f(i, j-1, s1, s2, dp)
                )
            return dp[i][j]
        return f(m-1, n-1, text1, text2, dp)

        m = len(text1)
        n = len(text2)
        dp = [
            [
                -1 for _ in range(n+1)
            ] for _ in range(m+1)
        ]
        for i in range(m+1): 
            dp[i][0] = 0
        for j in range(n+1): 
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]