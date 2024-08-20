class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        # brute force
        # arr = list(range(1, x+1))
        # for i in range(len(arr)-1, -1, -1):
        #     if arr[i]**2 <= x:
        #         return arr[i]

        # optimized - binary search
        l, r = 1, x
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if mid**2 <= x:
                if mid > ans:
                    ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
