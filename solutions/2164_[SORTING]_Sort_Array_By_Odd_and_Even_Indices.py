class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # odd indices: decresing
        # even indices: increasing

        # Brute Force: do a modified bubble sort for odd and even indices (i + 2)
        # TC: O(N^2) | SC: O(1)
        # n = len(nums)
        # for i in range(0, n, 2):
        #     for j in range(0, n-i-1, 2):
        #         if j + 2 < n and nums[j] > nums[j+2]:
        #             nums[j], nums[j+2] = nums[j+2], nums[j]
        # for i in range(1, n, 2):
        #     for j in range(1, n-i-1, 2):
        #         if j + 2 < n and nums[j] < nums[j+2]:
        #             nums[j], nums[j+2] = nums[j+2], nums[j]

        # Improved: Create two arrays for the odd and even indices, sort and merge them
        # TC: O(N log N) | SC: O(N)
        arr1 = [] # odd
        arr2 = [] # even
        for i in range(len(nums)):
            if i % 2:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        arr1.sort(reverse=True)
        arr2.sort()

        def merge(arr1, arr2):
            arr = []
            m, n = len(arr1), len(arr2)
            i, j = 0, 0
            while i < m and j < n:
                arr.append(arr2[j])
                j += 1
                arr.append(arr1[i])
                i += 1
            if (m + n) % 2:
                if i >= m: arr.append(arr2[j])
                if j >= n: arr.append(arr1[i])
            return arr

        return merge(arr1, arr2)
    
        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2])[::-1]

        return nums