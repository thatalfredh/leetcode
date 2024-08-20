class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # palindrome strings are the same reading from front and back
        # longest palindromic subsequence is equivalent to
        # longest common subsequence from a string and its reversed order

        # def LCS(s1, s2):
        #     if len(s1) == 0 or len(s2) == 0:
        #         return ""
        #     if s1[-1] == s2[-1]:
        #         return LCS(s1[:-1], s2[:-1]) + s1[-1]
        #     else:
        #         a = LCS(s1[:-1], s2)
        #         b = LCS(s1, s2[:-1])
        #         if len(a) > len(b):
        #             return a
        #         else:
        #             return b
        # lps = LCS(s, s[::-1])
        # return len(lps)

        s_ = s[::-1]
        n = len(s)
        dp = [
            [
                -1 for _ in range(n)
            ] for _ in range(n)
        ]
        def LCS(i, j, s1, s2, dp):
            if i < 0 or j < 0:
                return 0
            else:
                if dp[i][j] != -1:
                    return dp[i][j]
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + LCS(i-1, j-1, s1, s2, dp)
                else:
                    dp[i][j] = max(
                        LCS(i-1, j, s1, s2, dp), 
                        LCS(i, j-1, s1, s2, dp)
                    )
                return dp[i][j]

        return LCS(n-1, n-1, s, s_, dp)

        # s_ = s[::-1]
        # n = len(s)
        # dp = [
        #     [
        #         -1 for _ in range(n+1)
        #     ] for _ in range(n+1)
        # ]
        # for i in range(n+1):
        #     dp[i][0] = 0
        # for j in range(n+1):
        #     dp[0][j] = 0
        
        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         if s[i-1] == s_[j-1]:
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # return dp[n][n]