class Solution:
    def trap(self, height: List[int]) -> int:

        # intuition: water can only be trapped between decreasing followed by increasing sequence
        # water is trapped each time pillars x + k in between x and x + i are lesser than them for all k < i
        # in addition, we form a new "container" if f(x+k) > f(x) or f(x+k) > f(x+i)

        # volume = 0
        # i = 1
        # while i < len(height):
        #     # encounter decreasing sequence
        #     # expect to trap some water starting from here
        #     if height[i] < height[i-1]:
        #         v = 0
        #         j = i
        #         # terminate if found new max height for the current container
        #         while j < len(height) and height[j] <= height[i-1]:
        #             v += (height[i-1] - height[j])
        #             j += 1
        #         volume += v
        #         i = j + 1
        #     i += 1
        
        # brute logic above can be simplified
        # notice that at every point, the water trapped is always bounded by the min(left_max, right_max) - curr
        # we can pre-compute for every index, what are the left maximum and right maximum thus far

        # TC: O(n), SC: O(n)
        # left_max = []
        # right_max = []
        # lm = 0
        # for i in range(len(height)):
        #     if height[i] > lm:
        #         lm = height[i]
        #     left_max.append(lm)
        # rm = 0
        # for i in range(len(height)-1, -1, -1):
        #     if height[i] > rm:
        #         rm = height[i]
        #     right_max.append(rm)
        # right_max = right_max[::-1]
        # volume = 0 
        # for i in range(len(height)):
        #     volume += min(left_max[i], right_max[i]) - height[i]
        # return volume

        # optimal: O(n), O(1)
        volume = 0
        left_max = 0
        right_max = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                volume += left_max - height[l]
                l += 1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                volume += right_max - height[r]
                r -= 1
        return volume