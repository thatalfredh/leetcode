from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        What does preorder tell us? Postorder?
        - Preorder: It tells us the sequence of root nodes.
        - Postorder: The last node value in each L and R subtree represents the root of the subtree.
        > Unlike Problem 105 and 106, we do not immediately know the L and R separation in the Postorder array.

                    1
            2               3
        4       5       6       7
        Pre: [1, 2, 4, 5, 3, 6, 7]
        Post: [4, 5, 2, 6, 7, 3, 1]
                    1
            2               3
        4       5       
        Pre: [1, 2, 4, 5, 3]
        Post: [4, 5, 2, 3, 1]
                    1
            2               3
        4                       7
        Pre: [1, 2, 4, 3, 7]
        Post: [4, 2, 7, 3, 1]

        Given first root 1 in Preorder, we pass remaining  values in post for subsequent construction.
        Next, second root 2 in Preorder, remaining values are [4, 5]
        """
        # lookup = {y:x for x,y in enumerate(postorder)}
        # def buildFromPreAndPost(pre_start, pre_end, post_start, post_end):
        #     if post_end < post_start: return None
        #     if pre_end < pre_start: return None
        #     root = TreeNode(preorder[pre_start])
        #     if pre_end == pre_start: return root
        #     idx = lookup[preorder[pre_start + 1]]
        #     left_size = idx - post_start + 1
        #     root.left = buildFromPreAndPost(
        #         pre_start + 1, pre_start + left_size, 
        #         post_start, idx
        #     )
        #     root.right = buildFromPreAndPost(
        #         pre_start + 1 + left_size, pre_end, 
        #         idx + 1, post_end - 1
        #     )
        #     return root
        # return buildFromPreAndPost(0, len(preorder)-1, 0, len(postorder)-1)

        def buildFromPreAndPost(preorder, postorder):
            if not preorder: return None
            root = TreeNode(preorder[0])
            if len(preorder) == 1: return root
            idx = postorder.index(preorder[1])
            left = postorder[:idx+1]
            right = postorder[idx+1:-1]
            root.left = buildFromPreAndPost(preorder[1:len(left)+1], left)
            root.right = buildFromPreAndPost(preorder[len(left)+1:], right)
            return root

        return buildFromPreAndPost(preorder, postorder)

    # def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    #     if not preorder or not postorder:
    #         return
    #     root = TreeNode(preorder[0])
    #     if len(preorder) == 1:
    #         return root
    #     index = postorder.index(preorder[1])
    #     root.left = self.constructFromPrePost(preorder[1:index+2], postorder[:index+1])
    #     root.right = self.constructFromPrePost(preorder[index+2:], postorder[index+1:-1])
    #     return root
