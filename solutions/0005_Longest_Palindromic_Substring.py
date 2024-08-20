class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute Force: nest for-loop, get every possible substring
        # and check palindrome, update length
        # TC: O(n^3) | SC: O(1)

        # Improved: Every palindrome is either of odd or even length
        # For each element, we expand from a possible palindrome's center
        # i.e [i][i] or s[i][i+1]
        # Compare lengths of palindromes
        n = len(s)
        if n <= 1: return s
        max_str = s[0]
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(n-1):
            s1 = expand(i,i)
            s2 = expand(i, i+1)

            if len(s1) > len(max_str):
                max_str = s1
            if len(s2) > len(max_str):
                max_str = s2
        return max_str