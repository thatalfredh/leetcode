class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx_prod = -float("inf")

        # brute force for subarrays - generate all possible results
        # for i in range(0, len(nums)):
        #     prod = 1
        #     for j in range(i, len(nums)):
        #         prod *= nums[j]
        #         mx_prod = max(mx_prod, prod)

        # return mx_prod

        # optimize by "short circuiting" cases
        # 1. all positives, multiply all except 0
        # 2. even num of negatives, multiply all except 0
        # 3. odd num of negatives, the max product subarray should be separated by some negative number
        # 1 and 2 are special case of 3, no separation
        mx_prod = -float("inf")
        # num_negs = sum([x < 0 for x in nums])
        # if num_negs % 2 == 0:
        #     prod = 1
        #     for i in range(len(nums)):
        #         if prod == 0:
        #             prod = 1
        #         prod *= nums[i]
        #         mx_prod = max(mx_prod, prod)
        # else:
        left = 1
        right = 1
        for i in range(len(nums)):
            if left == 0: left = 1
            if right == 0: right = 1
            left *= nums[i]
            right *= nums[len(nums)-1-i]
            mx_prod = max(mx_prod, max(left, right))

        return mx_prod
