from typing import Optional
from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isPalindrome(self, x):
    #     return sum([i%2 for i in x]) <= 1

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        paths = 0
        # lookup = defaultdict(int)
        bit_vector = 0
        def dfs(node):
            nonlocal paths, bit_vector
            if not node: return
            # lookup[node.val] = lookup.get(node.val, 0) + 1
            bit_vector ^= 1 << node.val
            if not node.left and not node.right: # at leaf
                # counts = Counter(lookup.values())
                # if self.isPalindrome(lookup.values()): # palindrome; len(x) == 1 OR count(1) == 1 and 
                #     paths += 1
                if bit_vector == 0 or (bit_vector & (bit_vector - 1)) == 0:
                    paths += 1

            dfs(node.left)
            dfs(node.right)
            # lookup[node.val] -= 1
            bit_vector ^= 1 << node.val

        dfs(root)
        return paths
        