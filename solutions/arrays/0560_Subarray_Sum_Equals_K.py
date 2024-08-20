class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force: Nested for-loop to check all subarrays
        # n = len(nums)
        # cnt = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if sum(nums[i:j+1]) == k:
        #             cnt += 1
        # return cnt

        # Optimized: Checking all subarrays means recomputing results
        # Instead, we could store previous results and take difference
        n = len(nums)
        cnt = 0
        prefix_sum = 0
        sums_count = {0: 1} # e.g. if first 2 already made the sum
        for i in range(n):
            prefix_sum += nums[i]
            # check if current_sum - K is present previously
            # if yes, current element is last element of a subarray that sums to K
            if (prefix_sum - k) in sums_count: #in sums[:i]:
                cnt += sums_count[prefix_sum - k]
            
            # if prefix_sum in sums_count:
            #     sums_count[prefix_sum] += 1
            # else:
            #     sums_count[prefix_sum] = 1
            sums_count[prefix_sum] = sums_count.get(prefix_sum, 0) + 1

        return cnt