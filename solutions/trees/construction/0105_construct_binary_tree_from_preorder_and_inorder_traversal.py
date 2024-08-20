from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        What does preorder tell us? Inorder?
        - Preorder: Indicates the sequence of tree (and subtree) root
        - Inorder: Given the root, it indicates the separation between L and R subtrees
                    1
            2               3
        4       5       6       7
        Pre: [1, 2, 4, 5, 3, 6, 7]
        In: [4, 2, 5, 1, 6, 3, 7]

        Given first root 1 in Pre, separation in In is [4, 2, 5] and [6, 3, 7].
        Then next given 2, separation becomes [4] and [5].
        """
        in_lookup = {y:x for x,y in enumerate(inorder)}
        def buildFromPreAndIn(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            # Intuitive Approach:
            root = TreeNode(preorder[pre_start])
            idx = inorder.index(preorder[0])
            left = inorder[:idx] 
            right = inorder[idx+1:]
            root.left = buildFromPreAndIn(preorder[1:len(left)+1], left)
            root.right = buildFromPreAndIn(preorder[len(left)+1:], right)

            # Better Approach
            root = TreeNode(preorder[pre_start])
            idx = in_lookup[preorder[pre_start]] # O(1)
            left_size = idx - in_start # excluding the root value
            root.left = buildFromPreAndIn(
                pre_start + 1, 
                pre_start + left_size, 
                in_start, 
                idx-1
            )
            root.right = buildFromPreAndIn(
                pre_start + 1 + left_size, 
                pre_end, 
                idx + 1, 
                in_end
            )
            return root

        return buildFromPreAndIn(0, len(preorder)-1, 0, len(inorder)-1)