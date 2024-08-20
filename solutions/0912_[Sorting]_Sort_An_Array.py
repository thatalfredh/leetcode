class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(arr):
            n = len(arr)
            if n == 1:
                return arr
            left = mergesort(arr[:n//2])
            right = mergesort(arr[n//2:])
            return merge(left, right)
            
        def merge(left, right):
            m = len(left)
            n = len(right)
            i, j = 0, 0
            sorted_arr = []
            while i < m and j < n:
                if left[i] <= right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
                    
            if i < m: # values left on left array
                return sorted_arr + left[i:]
            else:
                return sorted_arr + right[j:]

        return mergesort(nums)


        
        
        