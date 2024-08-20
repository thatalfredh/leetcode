import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.map = {}
        for idx, n in enumerate(nums):
            if n not in self.map.keys():
                self.map[n] = []
            self.map[n].append(idx)

    def pick(self, target: int) -> int:
        # picks random index i from nums where nums[i] == target
        # the key to note here is the randomness is only applied for duplicate numbers
        return random.choice(self.map[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)